# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: gui\tabs\video_generator_tab.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
GUI Tab: Video Generator
- API Key (read-only) diisi otomatis setelah proses "create API key"
"""
from __future__ import annotations
import os
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
from datetime import datetime
from services.genai_video_service import GenAIVideoService
from services.video_postprocess_service import VideoPostprocessService
from typing import Optional, Callable


class VideoGeneratorTab:
    def __init__(self, root: tk.Misc, notebook: ttk.Notebook, log_fn, request_new_api_key_and_wait: Optional[Callable[[str, int], Optional[str]]] = None):
        self.root = root
        self.notebook = notebook
        self.log = log_fn
        self.request_new_api_key_and_wait = request_new_api_key_and_wait
        self.api_key_var = tk.StringVar()
        self.model_var = tk.StringVar(value='veo-3.0-generate-001')
        self.aspect_ratio_var = tk.StringVar(value='16:9')
        self.neg_prompt_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()
        self.image_to_video_var = tk.BooleanVar(value=False)
        self.veo2_double_var = tk.BooleanVar(value=False)
        self.veo3_audio_var = tk.BooleanVar(value=True)
        self.resolution_var = tk.StringVar(value='')
        self.prompt_count_var = tk.StringVar(value='Jumlah prompt: 0')
        self.prompts_text: Optional[scrolledtext.ScrolledText] = None
        self.progress_label: Optional[ttk.Label] = None
        self.start_btn: Optional[ttk.Button] = None
        self.stop_btn: Optional[ttk.Button] = None
        self._stop_event: Optional[threading.Event] = None
        self._worker_thread: Optional[threading.Thread] = None
        self._build_ui()

    def _build_ui(self):
        canvas_window = ttk.Frame(self.notebook)
        self.notebook.add(canvas_window, text='Video Generator')
        canvas = tk.Canvas(canvas_window, highlightthickness=0)
        vscroll = ttk.Scrollbar(canvas_window, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=vscroll.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        frame = ttk.Frame(canvas, padding=20)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        def _on_frame_configure(event=None):
            canvas.configure(scrollregion=canvas.bbox('all'))
            try:
                canvas.itemconfig('frame', width=canvas.winfo_width())
            except Exception:
                pass

        def _on_mousewheel(event):
            delta = event.delta
            if delta == 0 and hasattr(event, 'num'):
                delta = 120 if event.num == 4 else -120
            try:
                canvas.yview_scroll(int(-delta / 120), 'units')
            except Exception:
                pass

        frame.bind('<Configure>', _on_frame_configure)
        canvas.bind_all('<MouseWheel>', _on_mousewheel)
        canvas.bind_all('<Button-4>', _on_mousewheel)
        canvas.bind_all('<Button-5>', _on_mousewheel)

        api_frame = ttk.LabelFrame(frame, text='Google GenAI API Key (readonly)', padding=12)
        api_frame.pack(fill=X, pady=(0, 10))
        row = ttk.Frame(api_frame)
        row.pack(fill=X)
        entry = ttk.Entry(row, textvariable=self.api_key_var, width=60, state='readonly')
        entry.pack(side=LEFT, fill=X, expand=True)
        ttk.Button(row, text='Copy', width=10, command=self._on_copy_click, bootstyle=SECONDARY).pack(side=LEFT, padx=(8, 0))
        ttk.Button(row, text='Refresh', width=12, command=self._on_refresh_click, bootstyle=INFO).pack(side=LEFT, padx=(8, 0))

        opt = ttk.LabelFrame(frame, text='Options', padding=12)
        opt.pack(fill=X, pady=(0, 10))
        ttk.Label(opt, text='Model').grid(row=0, column=0, sticky=W)
        model_cb = ttk.Combobox(opt, textvariable=self.model_var, values=['veo-3.0-generate-001', 'veo-3.0-fast-generate-001', 'veo-2.0-generate-001'], state='readonly', width=28)
        model_cb.grid(row=0, column=1, sticky=W, padx=(8, 0))
        model_cb.bind('<<ComboboxSelected>>', lambda e: self._on_model_change())
        ttk.Label(opt, text='Aspect Ratio').grid(row=0, column=2, sticky=W, padx=(16, 0))
        ar_cb = ttk.Combobox(opt, textvariable=self.aspect_ratio_var, values=['16:9', '9:16'], state='readonly', width=10)
        ar_cb.grid(row=0, column=3, sticky=W, padx=(8, 0))
        ttk.Label(opt, text='Resolution').grid(row=1, column=0, sticky=W, pady=(8, 0))
        res_cb = ttk.Combobox(opt, textvariable=self.resolution_var, values=['', '1080p', '720p'], state='readonly', width=10)
        res_cb.grid(row=1, column=1, sticky=W, padx=(8, 0), pady=(8, 0))
        self.res_cb = res_cb
        ttk.Label(opt, text='Negative Prompt').grid(row=2, column=0, sticky=W, pady=(8, 0))
        neg_entry = ttk.Entry(opt, textvariable=self.neg_prompt_var)
        neg_entry.grid(row=2, column=1, columnspan=3, sticky=EW, padx=(8, 0), pady=(8, 0))
        cbar = ttk.Frame(opt)
        cbar.grid(row=3, column=0, columnspan=4, sticky=W, pady=(8, 0))
        ttk.Checkbutton(cbar, text='Veo 2: Generate 2 videos', variable=self.veo2_double_var, bootstyle='round-toggle').pack(side=LEFT)
        ttk.Checkbutton(cbar, text='Veo 3: Generate audio', variable=self.veo3_audio_var, bootstyle='round-toggle').pack(side=LEFT, padx=(16, 0))
        ttk.Checkbutton(cbar, text='Image-to-Video (Imagen 4 Ultra)', variable=self.image_to_video_var, bootstyle='round-toggle').pack(side=LEFT, padx=(16, 0))
        try:
            opt.columnconfigure(1, weight=1)
        except Exception:
            pass

        prm = ttk.LabelFrame(frame, text='Prompts (satu prompt per baris)', padding=12)
        prm.pack(fill=BOTH, expand=True, pady=(0, 10))
        self.prompts_text = scrolledtext.ScrolledText(prm, wrap=tk.WORD, height=8)
        self.prompts_text.pack(fill=BOTH, expand=True)
        try:
            self.prompts_text.bind('<KeyRelease>', lambda e: self._update_prompt_count())
        except Exception:
            pass
        btn_row = ttk.Frame(prm)
        btn_row.pack(fill=X, pady=(8, 0))
        ttk.Button(btn_row, text='Load from .txt', command=self._load_prompts_file, bootstyle=INFO).pack(side=LEFT)
        self.prompt_count_label = ttk.Label(btn_row, textvariable=self.prompt_count_var)
        self.prompt_count_label.pack(side=RIGHT)

        out = ttk.LabelFrame(frame, text='Output', padding=12)
        out.pack(fill=X, pady=(0, 10))
        ttk.Label(out, text='Folder').pack(anchor=W)
        row2 = ttk.Frame(out)
        row2.pack(fill=X)
        out_entry = ttk.Entry(row2, textvariable=self.output_dir_var)
        out_entry.pack(side=LEFT, fill=X, expand=True)
        ttk.Button(row2, text='Browse...', command=self._browse_output, bootstyle=INFO).pack(side=LEFT, padx=(8, 0))

        ctr = ttk.Frame(frame)
        ctr.pack(fill=X)
        self.start_btn = ttk.Button(ctr, text='Generate', bootstyle=SUCCESS, command=self._start_generation)
        self.start_btn.pack(side=LEFT)
        self.stop_btn = ttk.Button(ctr, text='Stop', bootstyle=DANGER, command=self._on_stop_click, state=DISABLED)
        self.stop_btn.pack(side=LEFT, padx=(8, 0))
        self.progress_label = ttk.Label(ctr, text='')
        self.progress_label.pack(side=LEFT, padx=(12, 0))
        self._on_model_change()
        try:
            self._update_prompt_count()
        except Exception:
            pass

    def _on_refresh_click(self):
        if (self.api_key_var.get() or '').strip():
            self._log('🔑 API key sudah terisi di form (readonly).')
        else:
            self._log('ℹ️ API key akan terisi otomatis setelah proses create API key dijalankan.')

    def _on_copy_click(self):
        key = (self.api_key_var.get() or '').strip()
        if not key:
            self._log('ℹ️ Tidak ada API key untuk disalin.')
            return
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(key)
            self.root.update()
            self._log('📋 API key disalin ke clipboard.')
        except Exception as e:
            self._log(f'⚠️ Gagal menyalin API key: {e}')

    def set_api_key(self, key: str):
        self.api_key_var.set((key or '').strip())
        if (self.api_key_var.get() or '').strip():
            self._log('🔑 API key diterima dan diisi ke form.')

    def _on_model_change(self):
        model = (self.model_var.get() or '').strip()
        if model.startswith('veo-2'):
            self.veo2_double_var.set(False)
        try:
            if model.startswith('veo-3'):
                self.res_cb.configure(state='readonly')
            else:
                self.res_cb.configure(state='disabled')
                self.resolution_var.set('')
        except Exception:
            pass

    def _load_prompts_file(self):
        try:
            filename = filedialog.askopenfilename(title='Pilih file .txt berisi prompts (satu per baris)', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
            if filename:
                content = Path(filename).read_text(encoding='utf-8')
                self.prompts_text.delete('1.0', tk.END)
                self.prompts_text.insert(tk.END, content)
                self._log(f'📄 Prompts dimuat dari: {filename}')
                self._update_prompt_count()
        except Exception as e:
            self._log(f'❌ Gagal load prompts: {e}')

    def _browse_output(self):
        try:
            folder = filedialog.askdirectory(title='Pilih folder output')
            if folder:
                self.output_dir_var.set(folder)
        except Exception as e:
            self._log(f'❌ Gagal memilih folder output: {e}')

    def _start_generation(self):
        try:
            self._update_prompt_count()
        except Exception:
            pass
        prompts = self._collect_prompts()
        if not prompts:
            messagebox.showwarning('Video Generator', 'Masukkan minimal satu prompt.')
            return
        if not (self.api_key_var.get() or '').strip():
            messagebox.showwarning('Video Generator', 'API key belum tersedia. Silakan jalankan proses create API key terlebih dahulu.')
            return
        out_dir = (self.output_dir_var.get() or '').strip()
        if not out_dir:
            messagebox.showwarning('Video Generator', 'Pilih folder output terlebih dahulu.')
            return
        Path(out_dir).mkdir(parents=True, exist_ok=True)
        model = (self.model_var.get() or '').strip()
        aspect = (self.aspect_ratio_var.get() or '').strip()
        neg = (self.neg_prompt_var.get() or '').strip() or None
        img2vid = bool(self.image_to_video_var.get())
        veo2_double = bool(self.veo2_double_var.get()) and model.startswith('veo-2')
        veo3_audio = bool(self.veo3_audio_var.get()) and model.startswith('veo-3')
        resolution = (self.resolution_var.get() or '').strip() or None if model.startswith('veo-3') else None
        self.start_btn.configure(state=DISABLED)
        try:
            self.stop_btn.configure(state=NORMAL)
        except Exception:
            pass
        self._stop_event = threading.Event()
        t = threading.Thread(target=self._worker_generate, args=(prompts, out_dir, model, aspect, neg, img2vid, veo2_double, veo3_audio, resolution), daemon=True)
        self._worker_thread = t
        t.start()

    def _worker_generate(self, prompts, out_dir, model, aspect, neg, img2vid, veo2_double, veo3_audio, resolution):
        try:
            svc = GenAIVideoService(api_key=(self.api_key_var.get() or '').strip())
            post = VideoPostprocessService()
            total = len(prompts)
            self._set_progress(f'Mulai generate {total} prompt...')
            for idx, prompt in enumerate(prompts, start=1):
                if self._stop_event and self._stop_event.is_set():
                    self._log('⏹️ Dihentikan oleh pengguna.')
                    break
                self._set_progress(f'[{idx}/{total}] Generating...')
                retried = False
                try:
                    image = None
                    if img2vid:
                        if self._stop_event and self._stop_event.is_set():
                            break
                        self._log('🖼️ Generating image via Imagen 4 Ultra...')
                        image = svc.generate_image_with_imagen(prompt=prompt, imagen_model='imagen-4.0-generate-001')
                    runs = 2 if veo2_double else 1
                    saved_paths = []
                    for r in range(1, runs + 1):
                        if self._stop_event and self._stop_event.is_set():
                            break
                        resp = svc.generate_video(prompt=prompt, model=model, aspect_ratio=aspect or None, negative_prompt=neg, image=image, resolution=resolution)
                        gen_videos = resp.get('generated_videos') or []
                        if not gen_videos:
                            raise RuntimeError('Tidak ada video pada response.')
                        safe_prefix = self._safe_name(prompt)[:40] or 'video'
                        base = datetime.now().strftime('%Y%m%d_%H%M%S')
                        suffix = f'_{r}' if runs > 1 else ''
                        paths = [str(Path(out_dir) / f'{base}{suffix}_{i + 1}_{safe_prefix}.mp4') for i in range(len(gen_videos))]
                        svc.download_videos(gen_videos, paths)
                        saved_paths.extend(paths[:len(gen_videos)])
                        if not veo3_audio and model.startswith('veo-3'):
                            for p in paths:
                                if self._stop_event and self._stop_event.is_set():
                                    break
                                try:
                                    post.remove_audio_inplace(p)
                                except Exception as e:
                                    self._log(f'⚠️ Gagal hapus audio: {e}')
                    self._log(f'✅ Selesai prompt {idx}/{total}. Files: {saved_paths}')
                except Exception as e:
                    err_msg = str(e)
                    self._log(f'❌ Gagal generate untuk prompt ke-{idx}: {e}')
                    if (not retried) and self._needs_new_api_key(err_msg) and self.request_new_api_key_and_wait:
                        new_key = self.request_new_api_key_and_wait(reason=err_msg, timeout_seconds=900)
                        if new_key:
                            try:
                                self.api_key_var.set(new_key)
                            except Exception:
                                pass
                            self._log('🔑 API key baru diterima. Melanjutkan otomatis...')
                            svc = GenAIVideoService(api_key=new_key)
                            retried = True
                            continue
        finally:
            self.root.after(0, lambda: self.start_btn.configure(state=NORMAL))
            try:
                self.root.after(0, lambda: self.stop_btn.configure(state=DISABLED))
            except Exception:
                pass
            if self._stop_event and self._stop_event.is_set():
                self._set_progress('Dihentikan oleh pengguna.')
            else:
                self._set_progress('Selesai.')

    def _on_stop_click(self):
        try:
            if not self._stop_event or not self._stop_event.is_set():
                self._stop_event.set()
                self._log('⏹️ Stop diminta. Menghentikan proses generate...')
                self.stop_btn.configure(state=DISABLED)
        except Exception as e:
            self._log(f'⚠️ Gagal meminta stop: {e}')

    def _collect_prompts(self):
        text = (self.prompts_text.get('1.0', tk.END) if self.prompts_text else '').strip()
        if not text:
            return []
        lines = [ln.strip() for ln in text.splitlines()]
        return [ln for ln in lines if ln]

    def _safe_name(self, s: str) -> str:
        invalid = '<>:"/\\|?*'
        for ch in invalid:
            s = s.replace(ch, ' ')
        s = ' '.join(s.split())
        return s.replace(' ', '_')

    def _set_progress(self, msg: str):
        self.root.after(0, lambda: self.progress_label.configure(text=msg))

    def _log(self, msg: str):
        self.root.after(0, lambda: self.log(msg))

    def _update_prompt_count(self):
        try:
            cnt = len(self._collect_prompts())
            self.prompt_count_var.set(f'Jumlah prompt: {cnt}')
        except Exception as e:
            self._log(f'⚠️ Gagal update jumlah prompt: {e}')

    def _needs_new_api_key(self, err_msg: str) -> bool:
        msg = (err_msg or '').lower()
        keywords = ['quota', 'exhaust', 'permission', 'forbidden', '403', '429', 'unauthorized', 'invalid api key', 'api key not valid', 'not have permission']
        return any((k in msg for k in keywords))