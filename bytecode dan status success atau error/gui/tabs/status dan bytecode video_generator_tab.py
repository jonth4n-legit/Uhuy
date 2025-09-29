Sorry: IndentationError: unexpected indent (indented_0.py, line 208)

<module>: Success: Equal

<module>.VideoGeneratorTab: Success: Equal

<module>.VideoGeneratorTab.__init__: Success: Equal

***<module>.VideoGeneratorTab._build_ui: Failure: Different bytecode

<module>.VideoGeneratorTab._build_ui._on_frame_configure: Success: Equal

***<module>.VideoGeneratorTab._build_ui._on_mousewheel: Failure detected at line number 79 and instruction offset 56: Different bytecode

<module>.VideoGeneratorTab._build_ui._bind_wheel: Success: Equal

<module>.VideoGeneratorTab._build_ui._unbind_wheel: Success: Equal

***<module>.VideoGeneratorTab._build_ui._update_scrollregion: Failure: Different bytecode

<module>.VideoGeneratorTab._build_ui.<lambda>: Success: Equal

<module>.VideoGeneratorTab._build_ui.<lambda>: Success: Equal

<module>.VideoGeneratorTab._build_ui.<lambda>: Success: Equal

<module>.VideoGeneratorTab._build_ui.<lambda>: Success: Equal

<module>.VideoGeneratorTab._on_refresh_click: Success: Equal

<module>.VideoGeneratorTab._on_copy_click: Success: Equal

<module>.VideoGeneratorTab.set_api_key: Success: Equal

<module>.VideoGeneratorTab._on_model_change: Success: Equal

***<module>.VideoGeneratorTab._load_prompts_file: Failure: Compilation Error

<module>.VideoGeneratorTab._browse_output: Success: Equal

<module>.VideoGeneratorTab._start_generation: Success: Equal

***<module>.VideoGeneratorTab._worker_generate: Failure: Compilation Error

***<module>.VideoGeneratorTab._worker_generate.<lambda>, None: Failure: Missing bytecode

***<module>.VideoGeneratorTab._worker_generate.<lambda>, None: Failure: Missing bytecode

***<module>.VideoGeneratorTab._worker_generate.<listcomp>, None: Failure: Missing bytecode

***<module>.VideoGeneratorTab._on_stop_click: Failure: Compilation Error

<module>.VideoGeneratorTab._collect_prompts: Success: Equal

<module>.VideoGeneratorTab._collect_prompts.<listcomp>: Success: Equal

<module>.VideoGeneratorTab._collect_prompts.<listcomp>: Success: Equal

<module>.VideoGeneratorTab._safe_name: Success: Equal

<module>.VideoGeneratorTab._set_progress: Success: Equal

<module>.VideoGeneratorTab._set_progress.<lambda>: Success: Equal

<module>.VideoGeneratorTab._log: Success: Equal

<module>.VideoGeneratorTab._log.<lambda>: Success: Equal

<module>.VideoGeneratorTab._update_prompt_count: Success: Equal

<module>.VideoGeneratorTab._needs_new_api_key: Success: Equal

<module>.VideoGeneratorTab._needs_new_api_key.<genexpr>: Success: Equal





0 LOAD_CONST 0 ('\nGUI Tab: Video Generator\n- API Key (read-only) diisi otomatis setelah proses "create API key" (bukan dari environment)\n- Pilihan model AI (Veo 3, Veo 3 Fast, Veo 2)\n- Aspect Ratio\n- Negative Prompt\n- Bulk prompt (textarea) + Load dari file .txt\n- Checkbox: Veo 2 -> generate 2 video\n- Checkbox: Veo 3 -> generate audio (default ON). Jika OFF, audio dihapus via ffmpeg (imageio-ffmpeg) setelah download.\n- Checkbox: Image-to-Video via Imagen 4 Ultra (generate image dari prompt lalu generate video via Veo 3)\n- Pilih folder output\n')
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (('annotations',))
8 IMPORT_NAME 1 (__future__)
10 IMPORT_FROM 2 (annotations)
12 STORE_NAME 2 (annotations)
14 POP_TOP

16 LOAD_CONST 1 (0)
18 LOAD_CONST 3 (None)
20 IMPORT_NAME 3 (os)
22 STORE_NAME 3 (os)

24 LOAD_CONST 1 (0)
26 LOAD_CONST 3 (None)
28 IMPORT_NAME 4 (threading)
30 STORE_NAME 4 (threading)

32 LOAD_CONST 1 (0)
34 LOAD_CONST 3 (None)
36 IMPORT_NAME 5 (tkinter)
38 STORE_NAME 6 (tk)

40 LOAD_CONST 1 (0)
42 LOAD_CONST 4 (('scrolledtext', 'filedialog', 'messagebox'))
44 IMPORT_NAME 5 (tkinter)
46 IMPORT_FROM 7 (scrolledtext)
48 STORE_NAME 7 (scrolledtext)
50 IMPORT_FROM 8 (filedialog)
52 STORE_NAME 8 (filedialog)
54 IMPORT_FROM 9 (messagebox)
56 STORE_NAME 9 (messagebox)
58 POP_TOP

60 LOAD_CONST 1 (0)
62 LOAD_CONST 3 (None)
64 IMPORT_NAME 10 (ttkbootstrap)
66 STORE_NAME 11 (ttk)

68 LOAD_CONST 1 (0)
70 LOAD_CONST 5 (('*',))
72 IMPORT_NAME 12 (ttkbootstrap.constants)
74 IMPORT_STAR

76 LOAD_CONST 1 (0)
78 LOAD_CONST 6 (('Path',))
80 IMPORT_NAME 13 (pathlib)
82 IMPORT_FROM 14 (Path)
84 STORE_NAME 14 (Path)
86 POP_TOP

88 LOAD_CONST 1 (0)
90 LOAD_CONST 7 (('datetime',))
92 IMPORT_NAME 15 (datetime)
94 IMPORT_FROM 15 (datetime)
96 STORE_NAME 15 (datetime)
98 POP_TOP

100 LOAD_CONST 1 (0)
102 LOAD_CONST 8 (('GenAIVideoService',))
104 IMPORT_NAME 16 (services.genai_video_service)
106 IMPORT_FROM 17 (GenAIVideoService)
108 STORE_NAME 17 (GenAIVideoService)
110 POP_TOP

112 LOAD_CONST 1 (0)
114 LOAD_CONST 9 (('VideoPostprocessService',))
116 IMPORT_NAME 18 (services.video_postprocess_service)
118 IMPORT_FROM 19 (VideoPostprocessService)
120 STORE_NAME 19 (VideoPostprocessService)
122 POP_TOP

124 LOAD_CONST 1 (0)
126 LOAD_CONST 10 (('Optional', 'Callable'))
128 IMPORT_NAME 20 (typing)
130 IMPORT_FROM 21 (Optional)
132 STORE_NAME 21 (Optional)
134 IMPORT_FROM 22 (Callable)
136 STORE_NAME 22 (Callable)
138 POP_TOP

140 PUSH_NULL
142 LOAD_BUILD_CLASS
144 LOAD_CONST 11 (code object VideoGeneratorTab)
146 MAKE_FUNCTION 0 (No arguments)
148 LOAD_CONST 12 ("VideoGeneratorTab")
150 CALL 2
152 STORE_NAME 23 (VideoGeneratorTab)
154 LOAD_CONST 3 (None)
156 RETURN_VALUE


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("VideoGeneratorTab")
6 STORE_NAME 2 (__qualname__)

8 LOAD_CONST 32 ((None,))
10 LOAD_CONST 33 (('root', 'tk.Misc', 'notebook', 'ttk.Notebook', 'request_new_api_key_and_wait', 'Optional[Callable[[str, int], Optional[str]]]'))
12 LOAD_CONST 8 (code object __init__)
14 MAKE_FUNCTION 5 (default, annotation)
16 STORE_NAME 3 (__init__)

18 LOAD_CONST 9 (code object _build_ui)
20 MAKE_FUNCTION 0 (No arguments)
22 STORE_NAME 4 (_build_ui)

24 LOAD_CONST 10 (code object _on_refresh_click)
26 MAKE_FUNCTION 0 (No arguments)
28 STORE_NAME 5 (_on_refresh_click)

30 LOAD_CONST 11 (code object _on_copy_click)
32 MAKE_FUNCTION 0 (No arguments)
34 STORE_NAME 6 (_on_copy_click)

36 LOAD_CONST 34 (('key', 'str'))
38 LOAD_CONST 14 (code object set_api_key)
40 MAKE_FUNCTION 4 (annotation)
42 STORE_NAME 7 (set_api_key)

44 LOAD_CONST 15 (code object _on_model_change)
46 MAKE_FUNCTION 0 (No arguments)
48 STORE_NAME 8 (_on_model_change)

50 LOAD_CONST 16 (code object _load_prompts_file)
52 MAKE_FUNCTION 0 (No arguments)
54 STORE_NAME 9 (_load_prompts_file)

56 LOAD_CONST 17 (code object _browse_output)
58 MAKE_FUNCTION 0 (No arguments)
60 STORE_NAME 10 (_browse_output)

62 LOAD_CONST 18 (code object _start_generation)
64 MAKE_FUNCTION 0 (No arguments)
66 STORE_NAME 11 (_start_generation)

68 LOAD_CONST 19 (code object _worker_generate)
70 MAKE_FUNCTION 0 (No arguments)
72 STORE_NAME 12 (_worker_generate)

74 LOAD_CONST 20 (code object _on_stop_click)
76 MAKE_FUNCTION 0 (No arguments)
78 STORE_NAME 13 (_on_stop_click)

80 LOAD_CONST 21 (code object _collect_prompts)
82 MAKE_FUNCTION 0 (No arguments)
84 STORE_NAME 14 (_collect_prompts)

86 LOAD_CONST 35 (('s', 'str', 'return', 'str'))
88 LOAD_CONST 24 (code object _safe_name)
90 MAKE_FUNCTION 4 (annotation)
92 STORE_NAME 15 (_safe_name)

94 LOAD_CONST 36 (('msg', 'str'))
96 LOAD_CONST 26 (code object _set_progress)
98 MAKE_FUNCTION 4 (annotation)
100 STORE_NAME 16 (_set_progress)

102 LOAD_CONST 36 (('msg', 'str'))
104 LOAD_CONST 27 (code object _log)
106 MAKE_FUNCTION 4 (annotation)
108 STORE_NAME 17 (_log)

110 LOAD_CONST 28 (code object _update_prompt_count)
112 MAKE_FUNCTION 0 (No arguments)
114 STORE_NAME 18 (_update_prompt_count)

116 LOAD_CONST 37 (('err_msg', 'str', 'return', 'bool'))
118 LOAD_CONST 31 (code object _needs_new_api_key)
120 MAKE_FUNCTION 4 (annotation)
122 STORE_NAME 19 (_needs_new_api_key)
124 LOAD_CONST 1 (None)
126 RETURN_VALUE


0 LOAD_FAST 1 (root)
2 LOAD_FAST 0 (self)
4 STORE_ATTR 0 (root)

6 LOAD_FAST 2 (notebook)
8 LOAD_FAST 0 (self)
10 STORE_ATTR 1 (notebook)

12 LOAD_FAST 3 (log_fn)
14 LOAD_FAST 0 (self)
16 STORE_ATTR 2 (log)

18 LOAD_FAST 4 (request_new_api_key_and_wait)
20 LOAD_FAST 0 (self)
22 STORE_ATTR 3 (request_new_api_key_and_wait)

24 LOAD_GLOBAL 9 (NULL + tk)
26 LOAD_ATTR 5 (StringVar)
28 CALL 0
30 LOAD_FAST 0 (self)
32 STORE_ATTR 6 (api_key_var)

34 LOAD_GLOBAL 9 (NULL + tk)
36 LOAD_ATTR 5 (StringVar)
38 LOAD_CONST 1 ("veo-3.0-generate-001")
40 KW_NAMES 2 (('value',))
42 CALL 1
44 LOAD_FAST 0 (self)
46 STORE_ATTR 7 (model_var)

48 LOAD_GLOBAL 9 (NULL + tk)
50 LOAD_ATTR 5 (StringVar)
52 LOAD_CONST 3 ("16:9")
54 KW_NAMES 2 (('value',))
56 CALL 1
58 LOAD_FAST 0 (self)
60 STORE_ATTR 8 (aspect_ratio_var)

62 LOAD_GLOBAL 9 (NULL + tk)
64 LOAD_ATTR 5 (StringVar)
66 CALL 0
68 LOAD_FAST 0 (self)
70 STORE_ATTR 9 (neg_prompt_var)

72 LOAD_GLOBAL 9 (NULL + tk)
74 LOAD_ATTR 5 (StringVar)
76 CALL 0
78 LOAD_FAST 0 (self)
80 STORE_ATTR 10 (output_dir_var)

82 LOAD_GLOBAL 9 (NULL + tk)
84 LOAD_ATTR 11 (BooleanVar)
86 LOAD_CONST 4 (False)
88 KW_NAMES 2 (('value',))
90 CALL 1
92 LOAD_FAST 0 (self)
94 STORE_ATTR 12 (image_to_video_var)

96 LOAD_GLOBAL 9 (NULL + tk)
98 LOAD_ATTR 11 (BooleanVar)
100 LOAD_CONST 4 (False)
102 KW_NAMES 2 (('value',))
104 CALL 1
106 LOAD_FAST 0 (self)
108 STORE_ATTR 13 (veo2_double_var)

110 LOAD_GLOBAL 9 (NULL + tk)
112 LOAD_ATTR 11 (BooleanVar)
114 LOAD_CONST 5 (True)
116 KW_NAMES 2 (('value',))
118 CALL 1
120 LOAD_FAST 0 (self)
122 STORE_ATTR 14 (veo3_audio_var)

124 LOAD_GLOBAL 9 (NULL + tk)
126 LOAD_ATTR 5 (StringVar)
128 LOAD_CONST 6 ("")
130 KW_NAMES 2 (('value',))
132 CALL 1
134 LOAD_FAST 0 (self)
136 STORE_ATTR 15 (resolution_var)

138 LOAD_GLOBAL 9 (NULL + tk)
140 LOAD_ATTR 5 (StringVar)
142 LOAD_CONST 7 ("Jumlah prompt: 0")
144 KW_NAMES 2 (('value',))
146 CALL 1
148 LOAD_FAST 0 (self)
150 STORE_ATTR 16 (prompt_count_var)

152 LOAD_CONST 0 (None)
154 LOAD_FAST 0 (self)
156 STORE_ATTR 17 (prompts_text)

158 LOAD_CONST 0 (None)
160 LOAD_FAST 0 (self)
162 STORE_ATTR 18 (progress_label)

164 LOAD_CONST 0 (None)
166 LOAD_FAST 0 (self)
168 STORE_ATTR 19 (start_btn)

170 LOAD_CONST 0 (None)
172 LOAD_FAST 0 (self)
174 STORE_ATTR 20 (stop_btn)

176 LOAD_CONST 0 (None)
178 LOAD_FAST 0 (self)
180 STORE_ATTR 21 (_stop_event)

182 LOAD_CONST 0 (None)
184 LOAD_FAST 0 (self)
186 STORE_ATTR 22 (_worker_thread)

188 LOAD_FAST 0 (self)
190 LOAD_METHOD 23 (_build_ui)
192 CALL 0
194 POP_TOP
196 LOAD_CONST 0 (None)
198 RETURN_VALUE


0 LOAD_GLOBAL 1 (NULL + ttk)
2 LOAD_ATTR 1 (Frame)
4 LOAD_DEREF 0 (self)
6 LOAD_ATTR 2 (notebook)
8 CALL 1
10 STORE_DEREF 25 (canvas_window)

12 LOAD_DEREF 0 (self)
14 LOAD_ATTR 2 (notebook)
16 LOAD_METHOD 3 (add)
18 LOAD_DEREF 25 (canvas_window)
20 LOAD_CONST 1 ("Video Generator")
22 KW_NAMES 2 (('text',))
24 CALL 2
26 POP_TOP

28 LOAD_GLOBAL 9 (NULL + tk)
30 LOAD_ATTR 5 (Canvas)
32 LOAD_DEREF 25 (canvas_window)
34 LOAD_CONST 3 (0)
36 KW_NAMES 4 (('highlightthickness',))
38 CALL 2
40 STORE_DEREF 23 (_update_scrollregion)

42 LOAD_GLOBAL 1 (NULL + ttk)
44 LOAD_ATTR 6 (Scrollbar)
46 LOAD_DEREF 25 (canvas_window)
48 LOAD_CONST 5 ("vertical")
50 LOAD_DEREF 23 (_update_scrollregion)
52 LOAD_ATTR 7 (yview)
54 KW_NAMES 6 (('orient', 'command'))
56 CALL 3
58 STORE_FAST 1 (vscroll)

60 LOAD_DEREF 23 (_update_scrollregion)
62 LOAD_METHOD 8 (configure)
64 LOAD_FAST 1 (vscroll)
66 LOAD_ATTR 9 (set)
68 KW_NAMES 7 (('yscrollcommand',))
70 CALL 1
72 POP_TOP

74 LOAD_DEREF 23 (_update_scrollregion)
76 LOAD_METHOD 10 (pack)
78 LOAD_GLOBAL 8 (tk)
80 LOAD_ATTR 11 (LEFT)
82 LOAD_GLOBAL 8 (tk)
84 LOAD_ATTR 12 (BOTH)
86 LOAD_CONST 8 (True)
88 KW_NAMES 9 (('side', 'fill', 'expand'))
90 CALL 3
92 POP_TOP

94 LOAD_FAST 1 (vscroll)
96 LOAD_METHOD 10 (pack)
98 LOAD_GLOBAL 8 (tk)
100 LOAD_ATTR 13 (RIGHT)
102 LOAD_GLOBAL 8 (tk)
104 LOAD_ATTR 14 (Y)
106 KW_NAMES 10 (('side', 'fill'))
108 CALL 2
110 POP_TOP

112 LOAD_GLOBAL 1 (NULL + ttk)
114 LOAD_ATTR 1 (Frame)
116 LOAD_DEREF 23 (_update_scrollregion)
118 LOAD_CONST 11 (20)
120 KW_NAMES 12 (('padding',))
122 CALL 2
124 STORE_FAST 2 (frame)

126 LOAD_DEREF 23 (_update_scrollregion)
128 LOAD_METHOD 15 (create_window)
130 LOAD_CONST 13 ((0, 0))
132 LOAD_FAST 2 (frame)
134 LOAD_CONST 14 ("nw")
136 KW_NAMES 15 (('window', 'anchor'))
138 CALL 3
140 STORE_DEREF 24 (canvas)

142 LOAD_CONST 93 ((None,))
144 LOAD_CLOSURE 23 (_update_scrollregion)
146 LOAD_CLOSURE 24 (canvas)
148 BUILD_TUPLE 2
150 LOAD_CONST 16 (code object _on_frame_configure)
152 MAKE_FUNCTION 9 (default, closure)
154 STORE_DEREF 20 (self)

156 LOAD_CLOSURE 23 (_update_scrollregion)
158 BUILD_TUPLE 1
160 LOAD_CONST 17 (code object _on_mousewheel)
162 MAKE_FUNCTION 8 (closure)
164 STORE_DEREF 21 (_on_frame_configure)

166 LOAD_FAST 2 (frame)
168 LOAD_METHOD 16 (bind)
170 LOAD_CONST 18 ("<Configure>")
172 LOAD_DEREF 20 (self)
174 CALL 2
176 POP_TOP

178 LOAD_CLOSURE 21 (_on_frame_configure)
180 LOAD_CLOSURE 23 (_update_scrollregion)
182 BUILD_TUPLE 2
184 LOAD_CONST 19 (code object _bind_wheel)
186 MAKE_FUNCTION 8 (closure)
188 STORE_FAST 3 (_bind_wheel)

190 LOAD_CLOSURE 23 (_update_scrollregion)
192 BUILD_TUPLE 1
194 LOAD_CONST 20 (code object _unbind_wheel)
196 MAKE_FUNCTION 8 (closure)
198 STORE_FAST 4 (_unbind_wheel)

200 LOAD_DEREF 23 (_update_scrollregion)
202 LOAD_METHOD 16 (bind)
204 LOAD_CONST 21 ("<Enter>")
206 LOAD_FAST 3 (_bind_wheel)
208 CALL 2
210 POP_TOP

212 LOAD_DEREF 23 (_update_scrollregion)
214 LOAD_METHOD 16 (bind)
216 LOAD_CONST 22 ("<Leave>")
218 LOAD_FAST 4 (_unbind_wheel)
220 CALL 2
222 POP_TOP

224 LOAD_CLOSURE 20 (self)
226 LOAD_CLOSURE 23 (_update_scrollregion)
228 LOAD_CLOSURE 25 (canvas_window)
230 BUILD_TUPLE 3
232 LOAD_CONST 23 (code object _update_scrollregion)
234 MAKE_FUNCTION 8 (closure)
236 STORE_DEREF 22 (_on_mousewheel)

238 LOAD_DEREF 25 (canvas_window)
240 LOAD_METHOD 16 (bind)
242 LOAD_CONST 24 ("<Visibility>")
244 LOAD_CLOSURE 22 (_on_mousewheel)
246 BUILD_TUPLE 1
248 LOAD_CONST 25 (code object <lambda>)
250 MAKE_FUNCTION 8 (closure)
252 CALL 2
254 POP_TOP

256 LOAD_DEREF 25 (canvas_window)
258 LOAD_METHOD 16 (bind)
260 LOAD_CONST 18 ("<Configure>")
262 LOAD_CLOSURE 22 (_on_mousewheel)
264 BUILD_TUPLE 1
266 LOAD_CONST 26 (code object <lambda>)
268 MAKE_FUNCTION 8 (closure)
270 CALL 2
272 POP_TOP

274 LOAD_DEREF 25 (canvas_window)
276 LOAD_METHOD 17 (after)
278 LOAD_CONST 3 (0)
280 LOAD_DEREF 22 (_on_mousewheel)
282 CALL 2
284 POP_TOP

286 LOAD_GLOBAL 1 (NULL + ttk)
288 LOAD_ATTR 18 (LabelFrame)
290 LOAD_FAST 2 (frame)
292 LOAD_CONST 27 ("Google GenAI API Key (readonly)")
294 LOAD_CONST 28 (12)
296 KW_NAMES 29 (('text', 'padding'))
298 CALL 3
300 STORE_FAST 5 (api_frame)

302 LOAD_FAST 5 (api_frame)
304 LOAD_METHOD 10 (pack)
306 LOAD_GLOBAL 38 (X)
308 LOAD_CONST 30 ((0, 10))
310 KW_NAMES 31 (('fill', 'pady'))
312 CALL 2
314 POP_TOP

316 LOAD_GLOBAL 1 (NULL + ttk)
318 LOAD_ATTR 1 (Frame)
320 LOAD_FAST 5 (api_frame)
322 CALL 1
324 STORE_FAST 6 (row)

326 LOAD_FAST 6 (row)
328 LOAD_METHOD 10 (pack)
330 LOAD_GLOBAL 38 (X)
332 KW_NAMES 32 (('fill',))
334 CALL 1
336 POP_TOP

338 LOAD_GLOBAL 1 (NULL + ttk)
340 LOAD_ATTR 20 (Entry)
342 LOAD_FAST 6 (row)
344 LOAD_DEREF 0 (self)
346 LOAD_ATTR 21 (api_key_var)
348 LOAD_CONST 33 (60)
350 LOAD_CONST 34 ("readonly")
352 KW_NAMES 35 (('textvariable', 'width', 'state'))
354 CALL 4
356 STORE_FAST 7 (entry)

358 LOAD_FAST 7 (entry)
360 LOAD_METHOD 10 (pack)
362 LOAD_GLOBAL 22 (LEFT)
364 LOAD_GLOBAL 38 (X)
366 LOAD_CONST 8 (True)
368 KW_NAMES 9 (('side', 'fill', 'expand'))
370 CALL 3
372 POP_TOP

374 LOAD_GLOBAL 1 (NULL + ttk)
376 LOAD_ATTR 22 (Button)
378 LOAD_FAST 6 (row)
380 LOAD_CONST 36 ("Copy")
382 LOAD_CONST 37 (10)
384 LOAD_DEREF 0 (self)
386 LOAD_ATTR 23 (_on_copy_click)
388 LOAD_GLOBAL 48 (SECONDARY)
390 KW_NAMES 38 (('text', 'width', 'command', 'bootstyle'))
392 CALL 5
394 LOAD_METHOD 10 (pack)
396 LOAD_GLOBAL 22 (LEFT)
398 LOAD_CONST 39 ((8, 0))
400 KW_NAMES 40 (('side', 'padx'))
402 CALL 2
404 POP_TOP

406 LOAD_GLOBAL 1 (NULL + ttk)
408 LOAD_ATTR 22 (Button)
410 LOAD_FAST 6 (row)
412 LOAD_CONST 41 ("Refresh")
414 LOAD_CONST 28 (12)
416 LOAD_DEREF 0 (self)
418 LOAD_ATTR 25 (_on_refresh_click)
420 LOAD_GLOBAL 52 (INFO)
422 KW_NAMES 38 (('text', 'width', 'command', 'bootstyle'))
424 CALL 5
426 LOAD_METHOD 10 (pack)
428 LOAD_GLOBAL 22 (LEFT)
430 LOAD_CONST 39 ((8, 0))
432 KW_NAMES 40 (('side', 'padx'))
434 CALL 2
436 POP_TOP

438 LOAD_GLOBAL 1 (NULL + ttk)
440 LOAD_ATTR 18 (LabelFrame)
442 LOAD_FAST 2 (frame)
444 LOAD_CONST 42 ("Options")
446 LOAD_CONST 28 (12)
448 KW_NAMES 29 (('text', 'padding'))
450 CALL 3
452 STORE_FAST 8 (opt)

454 LOAD_FAST 8 (opt)
456 LOAD_METHOD 10 (pack)
458 LOAD_GLOBAL 38 (X)
460 LOAD_CONST 30 ((0, 10))
462 KW_NAMES 31 (('fill', 'pady'))
464 CALL 2
466 POP_TOP

468 LOAD_GLOBAL 1 (NULL + ttk)
470 LOAD_ATTR 27 (Label)
472 LOAD_FAST 8 (opt)
474 LOAD_CONST 43 ("Model")
476 KW_NAMES 2 (('text',))
478 CALL 2
480 LOAD_METHOD 28 (grid)
482 LOAD_CONST 3 (0)
484 LOAD_CONST 3 (0)
486 LOAD_GLOBAL 58 (W)
488 KW_NAMES 44 (('row', 'column', 'sticky'))
490 CALL 3
492 POP_TOP

494 LOAD_GLOBAL 1 (NULL + ttk)
496 LOAD_ATTR 30 (Combobox)
498 LOAD_FAST 8 (opt)
500 LOAD_DEREF 0 (self)
502 LOAD_ATTR 31 (model_var)
504 BUILD_LIST 0
506 LOAD_CONST 45 (('veo-3.0-generate-001', 'veo-3.0-fast-generate-001', 'veo-2.0-generate-001'))
508 LIST_EXTEND 1

510 LOAD_CONST 34 ("readonly")
512 LOAD_CONST 46 (28)

514 KW_NAMES 47 (('textvariable', 'values', 'state', 'width'))
516 CALL 5
518 STORE_FAST 9 (model_cb)

520 LOAD_FAST 9 (model_cb)
522 LOAD_METHOD 28 (grid)
524 LOAD_CONST 3 (0)
526 LOAD_CONST 48 (1)
528 LOAD_GLOBAL 58 (W)
530 LOAD_CONST 39 ((8, 0))
532 KW_NAMES 49 (('row', 'column', 'sticky', 'padx'))
534 CALL 4
536 POP_TOP

538 LOAD_FAST 9 (model_cb)
540 LOAD_METHOD 16 (bind)
542 LOAD_CONST 50 ("<<ComboboxSelected>>")
544 LOAD_CLOSURE 0 (self)
546 BUILD_TUPLE 1
548 LOAD_CONST 51 (code object <lambda>)
550 MAKE_FUNCTION 8 (closure)
552 CALL 2
554 POP_TOP

556 LOAD_GLOBAL 1 (NULL + ttk)
558 LOAD_ATTR 27 (Label)
560 LOAD_FAST 8 (opt)
562 LOAD_CONST 52 ("Aspect Ratio")
564 KW_NAMES 2 (('text',))
566 CALL 2
568 LOAD_METHOD 28 (grid)
570 LOAD_CONST 3 (0)
572 LOAD_CONST 53 (2)
574 LOAD_GLOBAL 58 (W)
576 LOAD_CONST 54 ((16, 0))
578 KW_NAMES 49 (('row', 'column', 'sticky', 'padx'))
580 CALL 4
582 POP_TOP

584 LOAD_GLOBAL 1 (NULL + ttk)
586 LOAD_ATTR 30 (Combobox)
588 LOAD_FAST 8 (opt)
590 LOAD_DEREF 0 (self)
592 LOAD_ATTR 32 (aspect_ratio_var)
594 LOAD_CONST 55 ("16:9")
596 LOAD_CONST 56 ("9:16")
598 BUILD_LIST 2
600 LOAD_CONST 34 ("readonly")
602 LOAD_CONST 37 (10)
604 KW_NAMES 47 (('textvariable', 'values', 'state', 'width'))
606 CALL 5
608 STORE_FAST 10 (ar_cb)

610 LOAD_FAST 10 (ar_cb)
612 LOAD_METHOD 28 (grid)
614 LOAD_CONST 3 (0)
616 LOAD_CONST 57 (3)
618 LOAD_GLOBAL 58 (W)
620 LOAD_CONST 39 ((8, 0))
622 KW_NAMES 49 (('row', 'column', 'sticky', 'padx'))
624 CALL 4
626 POP_TOP

628 LOAD_GLOBAL 1 (NULL + ttk)
630 LOAD_ATTR 27 (Label)
632 LOAD_FAST 8 (opt)
634 LOAD_CONST 58 ("Resolution")
636 KW_NAMES 2 (('text',))
638 CALL 2
640 LOAD_METHOD 28 (grid)
642 LOAD_CONST 48 (1)
644 LOAD_CONST 3 (0)
646 LOAD_GLOBAL 58 (W)
648 LOAD_CONST 39 ((8, 0))
650 KW_NAMES 59 (('row', 'column', 'sticky', 'pady'))
652 CALL 4
654 POP_TOP

656 LOAD_GLOBAL 1 (NULL + ttk)
658 LOAD_ATTR 30 (Combobox)
660 LOAD_FAST 8 (opt)
662 LOAD_DEREF 0 (self)
664 LOAD_ATTR 33 (resolution_var)
666 BUILD_LIST 0
668 LOAD_CONST 60 (('', '1080p', '720p'))
670 LIST_EXTEND 1
672 LOAD_CONST 34 ("readonly")
674 LOAD_CONST 37 (10)
676 KW_NAMES 47 (('textvariable', 'values', 'state', 'width'))
678 CALL 5
680 STORE_FAST 11 (res_cb)

682 LOAD_FAST 11 (res_cb)
684 LOAD_METHOD 28 (grid)
686 LOAD_CONST 48 (1)
688 LOAD_CONST 48 (1)
690 LOAD_GLOBAL 58 (W)
692 LOAD_CONST 39 ((8, 0))
694 LOAD_CONST 39 ((8, 0))
696 KW_NAMES 61 (('row', 'column', 'sticky', 'padx', 'pady'))
698 CALL 5
700 POP_TOP

702 LOAD_FAST 11 (res_cb)
704 LOAD_DEREF 0 (self)
706 STORE_ATTR 34 (res_cb)

708 LOAD_GLOBAL 1 (NULL + ttk)
710 LOAD_ATTR 27 (Label)
712 LOAD_FAST 8 (opt)
714 LOAD_CONST 62 ("Negative Prompt")
716 KW_NAMES 2 (('text',))
718 CALL 2
720 LOAD_METHOD 28 (grid)
722 LOAD_CONST 53 (2)
724 LOAD_CONST 3 (0)
726 LOAD_GLOBAL 58 (W)
728 LOAD_CONST 39 ((8, 0))
730 KW_NAMES 59 (('row', 'column', 'sticky', 'pady'))
732 CALL 4
734 POP_TOP

736 LOAD_GLOBAL 1 (NULL + ttk)
738 LOAD_ATTR 20 (Entry)
740 LOAD_FAST 8 (opt)
742 LOAD_DEREF 0 (self)
744 LOAD_ATTR 35 (neg_prompt_var)
746 KW_NAMES 63 (('textvariable',))
748 CALL 2
750 STORE_FAST 12 (neg_entry)

752 LOAD_FAST 12 (neg_entry)
754 LOAD_METHOD 28 (grid)
756 LOAD_CONST 53 (2)
758 LOAD_CONST 48 (1)
760 LOAD_CONST 57 (3)
762 LOAD_GLOBAL 72 (EW)
764 LOAD_CONST 39 ((8, 0))
766 LOAD_CONST 39 ((8, 0))
768 KW_NAMES 64 (('row', 'column', 'columnspan', 'sticky', 'padx', 'pady'))
770 CALL 6
772 POP_TOP

774 LOAD_GLOBAL 1 (NULL + ttk)
776 LOAD_ATTR 1 (Frame)
778 LOAD_FAST 8 (opt)
780 CALL 1
782 STORE_FAST 13 (cbar)

784 LOAD_FAST 13 (cbar)
786 LOAD_METHOD 28 (grid)
788 LOAD_CONST 57 (3)
790 LOAD_CONST 3 (0)
792 LOAD_CONST 65 (4)
794 LOAD_GLOBAL 58 (W)
796 LOAD_CONST 39 ((8, 0))
798 KW_NAMES 66 (('row', 'column', 'columnspan', 'sticky', 'pady'))
800 CALL 5
802 POP_TOP

804 LOAD_GLOBAL 1 (NULL + ttk)
806 LOAD_ATTR 37 (Checkbutton)
808 LOAD_FAST 13 (cbar)
810 LOAD_CONST 67 ("Veo 2: Generate 2 videos")
812 LOAD_DEREF 0 (self)
814 LOAD_ATTR 38 (veo2_double_var)
816 LOAD_CONST 68 ("round-toggle")
818 KW_NAMES 69 (('text', 'variable', 'bootstyle'))
820 CALL 4
822 LOAD_METHOD 10 (pack)
824 LOAD_GLOBAL 22 (LEFT)
826 KW_NAMES 70 (('side',))
828 CALL 1
830 POP_TOP

832 LOAD_GLOBAL 1 (NULL + ttk)
834 LOAD_ATTR 37 (Checkbutton)
836 LOAD_FAST 13 (cbar)
838 LOAD_CONST 71 ("Veo 3: Generate audio")
840 LOAD_DEREF 0 (self)
842 LOAD_ATTR 39 (veo3_audio_var)
844 LOAD_CONST 68 ("round-toggle")
846 KW_NAMES 69 (('text', 'variable', 'bootstyle'))
848 CALL 4
850 LOAD_METHOD 10 (pack)
852 LOAD_GLOBAL 22 (LEFT)
854 LOAD_CONST 54 ((16, 0))
856 KW_NAMES 40 (('side', 'padx'))
858 CALL 2
860 POP_TOP

862 LOAD_GLOBAL 1 (NULL + ttk)
864 LOAD_ATTR 37 (Checkbutton)
866 LOAD_FAST 13 (cbar)
868 LOAD_CONST 72 ("Image-to-Video (Imagen 4 Ultra)")
870 LOAD_DEREF 0 (self)
872 LOAD_ATTR 40 (image_to_video_var)
874 LOAD_CONST 68 ("round-toggle")
876 KW_NAMES 69 (('text', 'variable', 'bootstyle'))
878 CALL 4
880 LOAD_METHOD 10 (pack)
882 LOAD_GLOBAL 22 (LEFT)
884 LOAD_CONST 54 ((16, 0))
886 KW_NAMES 40 (('side', 'padx'))
888 CALL 2
890 POP_TOP

892 NOP

894 LOAD_FAST 8 (opt)
896 LOAD_METHOD 41 (columnconfigure)
898 LOAD_CONST 48 (1)
900 LOAD_CONST 48 (1)
902 KW_NAMES 73 (('weight',))
904 CALL 2
906 POP_TOP
908 JUMP_FORWARD 16 (to 932)
910 PUSH_EXC_INFO

912 LOAD_GLOBAL 84 (Exception)
914 CHECK_EXC_MATCH
916 POP_JUMP_FORWARD_IF_FALSE 3 (to 924)
918 POP_TOP

920 POP_EXCEPT
922 JUMP_FORWARD 4 (to 932)

924 RERAISE 0
926 COPY 3
928 POP_EXCEPT
930 RERAISE 1

932 LOAD_GLOBAL 1 (NULL + ttk)
934 LOAD_ATTR 18 (LabelFrame)
936 LOAD_FAST 2 (frame)
938 LOAD_CONST 74 ("Prompts (satu prompt per baris)")
940 LOAD_CONST 28 (12)
942 KW_NAMES 29 (('text', 'padding'))
944 CALL 3
946 STORE_FAST 14 (prm)

948 LOAD_FAST 14 (prm)
950 LOAD_METHOD 10 (pack)
952 LOAD_GLOBAL 24 (BOTH)
954 LOAD_CONST 8 (True)
956 LOAD_CONST 30 ((0, 10))
958 KW_NAMES 75 (('fill', 'expand', 'pady'))
960 CALL 3
962 POP_TOP

964 LOAD_GLOBAL 87 (NULL + scrolledtext)
966 LOAD_ATTR 44 (ScrolledText)
968 LOAD_FAST 14 (prm)
970 LOAD_GLOBAL 8 (tk)
972 LOAD_ATTR 45 (WORD)
974 LOAD_CONST 76 (8)
976 KW_NAMES 77 (('wrap', 'height'))
978 CALL 3
980 LOAD_DEREF 0 (self)
982 STORE_ATTR 46 (prompts_text)

984 LOAD_DEREF 0 (self)
986 LOAD_ATTR 46 (prompts_text)
988 LOAD_METHOD 10 (pack)
990 LOAD_GLOBAL 24 (BOTH)
992 LOAD_CONST 8 (True)
994 KW_NAMES 78 (('fill', 'expand'))
996 CALL 2
998 POP_TOP

1000 NOP

1002 LOAD_DEREF 0 (self)
1004 LOAD_ATTR 46 (prompts_text)
1006 LOAD_METHOD 16 (bind)
1008 LOAD_CONST 79 ("<KeyRelease>")
1010 LOAD_CLOSURE 0 (self)
1012 BUILD_TUPLE 1
1014 LOAD_CONST 80 (code object <lambda>)
1016 MAKE_FUNCTION 8 (closure)
1018 CALL 2
1020 POP_TOP
1022 JUMP_FORWARD 16 (to 1046)
1024 PUSH_EXC_INFO

1026 LOAD_GLOBAL 84 (Exception)
1028 CHECK_EXC_MATCH
1030 POP_JUMP_FORWARD_IF_FALSE 3 (to 1038)
1032 POP_TOP

1034 POP_EXCEPT
1036 JUMP_FORWARD 4 (to 1046)

1038 RERAISE 0
1040 COPY 3
1042 POP_EXCEPT
1044 RERAISE 1

1046 LOAD_GLOBAL 1 (NULL + ttk)
1048 LOAD_ATTR 1 (Frame)
1050 LOAD_FAST 14 (prm)
1052 CALL 1
1054 STORE_FAST 15 (btn_row)

1056 LOAD_FAST 15 (btn_row)
1058 LOAD_METHOD 10 (pack)
1060 LOAD_GLOBAL 38 (X)
1062 LOAD_CONST 39 ((8, 0))
1064 KW_NAMES 31 (('fill', 'pady'))
1066 CALL 2
1068 POP_TOP

1070 LOAD_GLOBAL 1 (NULL + ttk)
1072 LOAD_ATTR 22 (Button)
1074 LOAD_FAST 15 (btn_row)
1076 LOAD_CONST 81 ("Load from .txt")
1078 LOAD_DEREF 0 (self)
1080 LOAD_ATTR 47 (_load_prompts_file)
1082 LOAD_GLOBAL 52 (INFO)
1084 KW_NAMES 82 (('text', 'command', 'bootstyle'))
1086 CALL 4
1088 LOAD_METHOD 10 (pack)
1090 LOAD_GLOBAL 22 (LEFT)
1092 KW_NAMES 70 (('side',))
1094 CALL 1
1096 POP_TOP

1098 LOAD_GLOBAL 1 (NULL + ttk)
1100 LOAD_ATTR 27 (Label)
1102 LOAD_FAST 15 (btn_row)
1104 LOAD_DEREF 0 (self)
1106 LOAD_ATTR 48 (prompt_count_var)
1108 KW_NAMES 63 (('textvariable',))
1110 CALL 2
1112 LOAD_DEREF 0 (self)
1114 STORE_ATTR 49 (prompt_count_label)

1116 LOAD_DEREF 0 (self)
1118 LOAD_ATTR 49 (prompt_count_label)
1120 LOAD_METHOD 10 (pack)
1122 LOAD_GLOBAL 26 (RIGHT)
1124 KW_NAMES 70 (('side',))
1126 CALL 1
1128 POP_TOP

1130 LOAD_GLOBAL 1 (NULL + ttk)
1132 LOAD_ATTR 18 (LabelFrame)
1134 LOAD_FAST 2 (frame)
1136 LOAD_CONST 83 ("Output")
1138 LOAD_CONST 28 (12)
1140 KW_NAMES 29 (('text', 'padding'))
1142 CALL 3
1144 STORE_FAST 16 (out)

1146 LOAD_FAST 16 (out)
1148 LOAD_METHOD 10 (pack)
1150 LOAD_GLOBAL 38 (X)
1152 LOAD_CONST 30 ((0, 10))
1154 KW_NAMES 31 (('fill', 'pady'))
1156 CALL 2
1158 POP_TOP

1160 LOAD_GLOBAL 1 (NULL + ttk)
1162 LOAD_ATTR 27 (Label)
1164 LOAD_FAST 16 (out)
1166 LOAD_CONST 84 ("Folder")
1168 KW_NAMES 2 (('text',))
1170 CALL 2
1172 LOAD_METHOD 10 (pack)
1174 LOAD_GLOBAL 58 (W)
1176 KW_NAMES 85 (('anchor',))
1178 CALL 1
1180 POP_TOP

1182 LOAD_GLOBAL 1 (NULL + ttk)
1184 LOAD_ATTR 1 (Frame)
1186 LOAD_FAST 16 (out)
1188 CALL 1
1190 STORE_FAST 17 (row2)

1192 LOAD_FAST 17 (row2)
1194 LOAD_METHOD 10 (pack)
1196 LOAD_GLOBAL 38 (X)
1198 KW_NAMES 32 (('fill',))
1200 CALL 1
1202 POP_TOP

1204 LOAD_GLOBAL 1 (NULL + ttk)
1206 LOAD_ATTR 20 (Entry)
1208 LOAD_FAST 17 (row2)
1210 LOAD_DEREF 0 (self)
1212 LOAD_ATTR 50 (output_dir_var)
1214 KW_NAMES 63 (('textvariable',))
1216 CALL 2
1218 STORE_FAST 18 (out_entry)

1220 LOAD_FAST 18 (out_entry)
1222 LOAD_METHOD 10 (pack)
1224 LOAD_GLOBAL 22 (LEFT)
1226 LOAD_GLOBAL 38 (X)
1228 LOAD_CONST 8 (True)
1230 KW_NAMES 9 (('side', 'fill', 'expand'))
1232 CALL 3
1234 POP_TOP

1236 LOAD_GLOBAL 1 (NULL + ttk)
1238 LOAD_ATTR 22 (Button)
1240 LOAD_FAST 17 (row2)
1242 LOAD_CONST 86 ("Browse...")
1244 LOAD_DEREF 0 (self)
1246 LOAD_ATTR 51 (_browse_output)
1248 LOAD_GLOBAL 52 (INFO)
1250 KW_NAMES 82 (('text', 'command', 'bootstyle'))
1252 CALL 4
1254 LOAD_METHOD 10 (pack)
1256 LOAD_GLOBAL 22 (LEFT)
1258 LOAD_CONST 39 ((8, 0))
1260 KW_NAMES 40 (('side', 'padx'))
1262 CALL 2
1264 POP_TOP

1266 LOAD_GLOBAL 1 (NULL + ttk)
1268 LOAD_ATTR 1 (Frame)
1270 LOAD_FAST 2 (frame)
1272 CALL 1
1274 STORE_FAST 19 (ctr)

1276 LOAD_FAST 19 (ctr)
1278 LOAD_METHOD 10 (pack)
1280 LOAD_GLOBAL 38 (X)
1282 KW_NAMES 32 (('fill',))
1284 CALL 1
1286 POP_TOP

1288 LOAD_GLOBAL 1 (NULL + ttk)
1290 LOAD_ATTR 22 (Button)
1292 LOAD_FAST 19 (ctr)
1294 LOAD_CONST 87 ("Generate")
1296 LOAD_GLOBAL 104 (SUCCESS)
1298 LOAD_DEREF 0 (self)
1300 LOAD_ATTR 53 (_start_generation)
1302 KW_NAMES 88 (('text', 'bootstyle', 'command'))
1304 CALL 4
1306 LOAD_DEREF 0 (self)
1308 STORE_ATTR 54 (start_btn)

1310 LOAD_DEREF 0 (self)
1312 LOAD_ATTR 54 (start_btn)
1314 LOAD_METHOD 10 (pack)
1316 LOAD_GLOBAL 22 (LEFT)
1318 KW_NAMES 70 (('side',))
1320 CALL 1
1322 POP_TOP

1324 LOAD_GLOBAL 1 (NULL + ttk)
1326 LOAD_ATTR 22 (Button)
1328 LOAD_FAST 19 (ctr)
1330 LOAD_CONST 89 ("Stop")
1332 LOAD_GLOBAL 110 (DANGER)
1334 LOAD_DEREF 0 (self)
1336 LOAD_ATTR 56 (_on_stop_click)
1338 LOAD_GLOBAL 114 (DISABLED)
1340 KW_NAMES 90 (('text', 'bootstyle', 'command', 'state'))
1342 CALL 5
1344 LOAD_DEREF 0 (self)
1346 STORE_ATTR 58 (stop_btn)

1348 LOAD_DEREF 0 (self)
1350 LOAD_ATTR 58 (stop_btn)
1352 LOAD_METHOD 10 (pack)
1354 LOAD_GLOBAL 22 (LEFT)
1356 LOAD_CONST 39 ((8, 0))
1358 KW_NAMES 40 (('side', 'padx'))
1360 CALL 2
1362 POP_TOP

1364 LOAD_GLOBAL 1 (NULL + ttk)
1366 LOAD_ATTR 27 (Label)
1368 LOAD_FAST 19 (ctr)
1370 LOAD_CONST 91 ("")
1372 KW_NAMES 2 (('text',))
1374 CALL 2
1376 LOAD_DEREF 0 (self)
1378 STORE_ATTR 59 (progress_label)

1380 LOAD_DEREF 0 (self)
1382 LOAD_ATTR 59 (progress_label)
1384 LOAD_METHOD 10 (pack)
1386 LOAD_GLOBAL 22 (LEFT)
1388 LOAD_CONST 92 ((12, 0))
1390 KW_NAMES 40 (('side', 'padx'))
1392 CALL 2
1394 POP_TOP

1396 LOAD_DEREF 0 (self)
1398 LOAD_METHOD 60 (_on_model_change)
1400 CALL 0
1402 POP_TOP

1404 NOP

1406 LOAD_DEREF 0 (self)
1408 LOAD_METHOD 61 (_update_prompt_count)
1410 CALL 0
1412 POP_TOP
1414 LOAD_CONST 0 (None)
1416 RETURN_VALUE
1418 PUSH_EXC_INFO

1420 LOAD_GLOBAL 84 (Exception)
1422 CHECK_EXC_MATCH
1424 POP_JUMP_FORWARD_IF_FALSE 4 (to 1434)
1426 POP_TOP

1428 POP_EXCEPT
1430 LOAD_CONST 0 (None)
1432 RETURN_VALUE

1434 RERAISE 0
1436 COPY 3
1438 POP_EXCEPT
1440 RERAISE 1

0 COPY_FREE_VARS 2

2 LOAD_DEREF 1 (canvas)
4 LOAD_METHOD 0 (configure)
6 LOAD_DEREF 1 (canvas)
8 LOAD_METHOD 1 (bbox)
10 LOAD_CONST 1 ("all")
12 CALL 1
14 KW_NAMES 2 (('scrollregion',))
16 CALL 1
18 POP_TOP

20 NOP

22 LOAD_DEREF 1 (canvas)
24 LOAD_METHOD 2 (itemconfig)
26 LOAD_DEREF 2 (canvas_window)
28 LOAD_DEREF 1 (canvas)
30 LOAD_METHOD 3 (winfo_width)
32 CALL 0
34 KW_NAMES 3 (('width',))
36 CALL 2
38 POP_TOP
40 LOAD_CONST 0 (None)
42 RETURN_VALUE
44 PUSH_EXC_INFO

46 LOAD_GLOBAL 8 (Exception)
48 CHECK_EXC_MATCH
50 POP_JUMP_FORWARD_IF_FALSE 4 (to 60)
52 POP_TOP

54 POP_EXCEPT
56 LOAD_CONST 0 (None)
58 RETURN_VALUE

60 RERAISE 0
62 COPY 3
64 POP_EXCEPT
66 RERAISE 1

0 COPY_FREE_VARS 1

2 LOAD_FAST 0 (event)
4 LOAD_ATTR 0 (delta)
6 STORE_FAST 1 (delta)

8 LOAD_FAST 1 (delta)
10 LOAD_CONST 1 (0)
12 COMPARE_OP 2 (==)
14 POP_JUMP_FORWARD_IF_FALSE 31 (to 44)
16 LOAD_GLOBAL 3 (NULL + hasattr)
18 LOAD_FAST 0 (event)
20 LOAD_CONST 2 ("num")
22 CALL 2
24 POP_JUMP_FORWARD_IF_FALSE 15 (to 44)

26 LOAD_FAST 0 (event)
28 LOAD_ATTR 2 (num)
30 LOAD_CONST 3 (4)
32 COMPARE_OP 2 (==)
34 POP_JUMP_FORWARD_IF_FALSE 2 (to 40)
36 LOAD_CONST 4 (120)
38 JUMP_FORWARD 1 (to 42)
40 LOAD_CONST 5 (-120)
42 STORE_FAST 1 (delta)

44 NOP

46 LOAD_DEREF 2 (canvas)
48 LOAD_METHOD 3 (yview_scroll)
50 LOAD_GLOBAL 9 (NULL + int)
52 LOAD_FAST 1 (delta)
54 UNARY_NEGATIVE
56 LOAD_CONST 4 (120)
58 BINARY_OP 11
60 CALL 1
62 LOAD_CONST 6 ("units")
64 CALL 2
66 POP_TOP
68 LOAD_CONST 0 (None)
70 RETURN_VALUE
72 PUSH_EXC_INFO

74 LOAD_GLOBAL 10 (Exception)
76 CHECK_EXC_MATCH
78 POP_JUMP_FORWARD_IF_FALSE 4 (to 88)
80 POP_TOP

82 POP_EXCEPT
84 LOAD_CONST 0 (None)
86 RETURN_VALUE

88 RERAISE 0
90 COPY 3
92 POP_EXCEPT
94 RERAISE 1

0 COPY_FREE_VARS 2

2 LOAD_DEREF 2 (canvas)
4 LOAD_METHOD 0 (bind_all)
6 LOAD_CONST 1 ("<MouseWheel>")
8 LOAD_DEREF 1 (_on_mousewheel)
10 CALL 2
12 POP_TOP

14 LOAD_DEREF 2 (canvas)
16 LOAD_METHOD 0 (bind_all)
18 LOAD_CONST 2 ("<Button-4>")
20 LOAD_DEREF 1 (_on_mousewheel)
22 CALL 2
24 POP_TOP

26 LOAD_DEREF 2 (canvas)
28 LOAD_METHOD 0 (bind_all)
30 LOAD_CONST 3 ("<Button-5>")
32 LOAD_DEREF 1 (_on_mousewheel)
34 CALL 2
36 POP_TOP
38 LOAD_CONST 0 (None)
40 RETURN_VALUE

0 COPY_FREE_VARS 1

2 LOAD_DEREF 1 (canvas)
4 LOAD_METHOD 0 (unbind_all)
6 LOAD_CONST 1 ("<MouseWheel>")
8 CALL 1
10 POP_TOP

12 LOAD_DEREF 1 (canvas)
14 LOAD_METHOD 0 (unbind_all)
16 LOAD_CONST 2 ("<Button-4>")
18 CALL 1
20 POP_TOP

22 LOAD_DEREF 1 (canvas)
24 LOAD_METHOD 0 (unbind_all)
26 LOAD_CONST 3 ("<Button-5>")
28 CALL 1
30 POP_TOP
32 LOAD_CONST 0 (None)
34 RETURN_VALUE

0 COPY_FREE_VARS 3

2 NOP

4 LOAD_DEREF 2 (outer)
6 LOAD_METHOD 0 (update_idletasks)
8 CALL 0
10 POP_TOP

12 PUSH_NULL
14 LOAD_DEREF 0 (_on_frame_configure)
16 CALL 0
18 POP_TOP

20 LOAD_DEREF 1 (canvas)
22 LOAD_METHOD 1 (yview_moveto)
24 LOAD_CONST 1 (0.0)
26 CALL 1
28 POP_TOP
30 LOAD_CONST 0 (None)
32 RETURN_VALUE
34 PUSH_EXC_INFO

36 LOAD_GLOBAL 4 (Exception)
38 CHECK_EXC_MATCH
40 POP_JUMP_FORWARD_IF_FALSE 4 (to 50)
42 POP_TOP

44 POP_EXCEPT
46 LOAD_CONST 0 (None)
48 RETURN_VALUE

50 RERAISE 0
52 COPY 3
54 POP_EXCEPT
56 RERAISE 1

0 COPY_FREE_VARS 1

2 PUSH_NULL
4 LOAD_DEREF 1 (_update_scrollregion)
6 CALL 0
8 RETURN_VALUE

0 COPY_FREE_VARS 1

2 PUSH_NULL
4 LOAD_DEREF 1 (_update_scrollregion)
6 CALL 0
8 RETURN_VALUE

0 COPY_FREE_VARS 1

2 LOAD_DEREF 1 (self)
4 LOAD_METHOD 0 (_on_model_change)
6 CALL 0
8 RETURN_VALUE

0 COPY_FREE_VARS 1

2 LOAD_DEREF 1 (self)
4 LOAD_METHOD 0 (_update_prompt_count)
6 CALL 0
8 RETURN_VALUE


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (api_key_var)
4 LOAD_METHOD 1 (get)
6 CALL 0
8 JUMP_IF_TRUE_OR_POP 1 (to 12)
10 LOAD_CONST 1 ("")
12 LOAD_METHOD 2 (strip)
14 CALL 0
16 POP_JUMP_FORWARD_IF_FALSE 23 (to 32)

18 LOAD_FAST 0 (self)
20 LOAD_METHOD 3 (_log)
22 LOAD_CONST 2 ("🔑 API key sudah terisi di form (readonly).")
24 CALL 1
26 POP_TOP
28 LOAD_CONST 0 (None)
30 RETURN_VALUE

32 LOAD_FAST 0 (self)
34 LOAD_METHOD 3 (_log)
36 LOAD_CONST 3 ("ℹ️ API key akan terisi otomatis setelah proses create API key dijalankan.")
38 CALL 1
40 POP_TOP
42 LOAD_CONST 0 (None)
44 RETURN_VALUE


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (api_key_var)
4 LOAD_METHOD 1 (get)
6 CALL 0
8 JUMP_IF_TRUE_OR_POP 1 (to 12)
10 LOAD_CONST 1 ("")
12 LOAD_METHOD 2 (strip)
14 CALL 0
16 STORE_FAST 1 (key)

18 LOAD_FAST 1 (key)
20 POP_JUMP_FORWARD_IF_TRUE 23 (to 36)

22 LOAD_FAST 0 (self)
24 LOAD_METHOD 3 (_log)
26 LOAD_CONST 2 ("ℹ️ Tidak ada API key untuk disalin.")
28 CALL 1
30 POP_TOP

32 LOAD_CONST 0 (None)
34 RETURN_VALUE

36 NOP

38 LOAD_FAST 0 (self)
40 LOAD_ATTR 4 (root)
42 LOAD_METHOD 5 (clipboard_clear)
44 CALL 0
46 POP_TOP

48 LOAD_FAST 0 (self)
50 LOAD_ATTR 4 (root)
52 LOAD_METHOD 6 (clipboard_append)
54 LOAD_FAST 1 (key)
56 CALL 1
58 POP_TOP

60 LOAD_FAST 0 (self)
62 LOAD_ATTR 4 (root)
64 LOAD_METHOD 7 (update)
66 CALL 0
68 POP_TOP

70 LOAD_FAST 0 (self)
72 LOAD_METHOD 3 (_log)
74 LOAD_CONST 3 ("📋 API key disalin ke clipboard.")
76 CALL 1
78 POP_TOP
80 LOAD_CONST 0 (None)
82 RETURN_VALUE
84 PUSH_EXC_INFO

86 LOAD_GLOBAL 16 (Exception)
88 CHECK_EXC_MATCH
90 POP_JUMP_FORWARD_IF_FALSE 35 (to 130)
92 STORE_FAST 2 (e)

94 LOAD_FAST 0 (self)
96 LOAD_METHOD 3 (_log)
98 LOAD_CONST 4 ("⚠️ Gagal menyalin API key: ")
100 LOAD_FAST 2 (e)
102 FORMAT_VALUE 0
104 BUILD_STRING 2
106 CALL 1
108 POP_TOP
110 POP_EXCEPT
112 LOAD_CONST 0 (None)
114 STORE_FAST 2 (e)
116 DELETE_FAST 2 (e)
118 LOAD_CONST 0 (None)
120 RETURN_VALUE
122 LOAD_CONST 0 (None)
124 STORE_FAST 2 (e)
126 DELETE_FAST 2 (e)
128 RERAISE 1

130 RERAISE 0
132 COPY 3
134 POP_EXCEPT
136 RERAISE 1


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (api_key_var)
4 LOAD_METHOD 1 (set)
6 LOAD_FAST 1 (key)
8 JUMP_IF_TRUE_OR_POP 1 (to 12)
10 LOAD_CONST 1 ("")
12 LOAD_METHOD 2 (strip)
14 CALL 0
16 CALL 1
18 POP_TOP

20 LOAD_FAST 0 (self)
22 LOAD_ATTR 0 (api_key_var)
24 LOAD_METHOD 3 (get)
26 CALL 0
28 JUMP_IF_TRUE_OR_POP 1 (to 32)
30 LOAD_CONST 1 ("")
32 LOAD_METHOD 2 (strip)
34 CALL 0
36 POP_JUMP_FORWARD_IF_FALSE 23 (to 52)

38 LOAD_FAST 0 (self)
40 LOAD_METHOD 4 (_log)
42 LOAD_CONST 2 ("🔑 API key diterima dan diisi ke form.")
44 CALL 1
46 POP_TOP
48 LOAD_CONST 3 (None)
50 RETURN_VALUE

52 LOAD_CONST 3 (None)
54 RETURN_VALUE


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (model_var)
4 LOAD_METHOD 1 (get)
6 CALL 0
8 JUMP_IF_TRUE_OR_POP 1 (to 12)
10 LOAD_CONST 1 ("")
12 LOAD_METHOD 2 (strip)
14 CALL 0
16 STORE_FAST 1 (model)

18 LOAD_FAST 1 (model)
20 LOAD_METHOD 3 (startswith)
22 LOAD_CONST 2 ("veo-2")
24 CALL 1
26 POP_JUMP_FORWARD_IF_FALSE 26 (to 40)

28 LOAD_FAST 0 (self)
30 LOAD_ATTR 4 (veo2_double_var)
32 LOAD_METHOD 5 (set)
34 LOAD_CONST 3 (False)
36 CALL 1
38 POP_TOP

40 NOP

42 LOAD_FAST 1 (model)
44 LOAD_METHOD 3 (startswith)
46 LOAD_CONST 4 ("veo-3")
48 CALL 1
50 POP_JUMP_FORWARD_IF_FALSE 29 (to 70)

52 LOAD_FAST 0 (self)
54 LOAD_ATTR 6 (res_cb)
56 LOAD_METHOD 7 (configure)
58 LOAD_CONST 5 ("readonly")
60 KW_NAMES 6 (('state',))
62 CALL 1
64 POP_TOP
66 LOAD_CONST 0 (None)
68 RETURN_VALUE

70 LOAD_FAST 0 (self)
72 LOAD_ATTR 6 (res_cb)
74 LOAD_METHOD 7 (configure)
76 LOAD_CONST 7 ("disabled")
78 KW_NAMES 6 (('state',))
80 CALL 1
82 POP_TOP

84 LOAD_FAST 0 (self)
86 LOAD_ATTR 8 (resolution_var)
88 LOAD_METHOD 5 (set)
90 LOAD_CONST 1 ("")
92 CALL 1
94 POP_TOP
96 LOAD_CONST 0 (None)
98 RETURN_VALUE
100 PUSH_EXC_INFO

102 LOAD_GLOBAL 18 (Exception)
104 CHECK_EXC_MATCH
106 POP_JUMP_FORWARD_IF_FALSE 4 (to 116)
108 POP_TOP

110 POP_EXCEPT
112 LOAD_CONST 0 (None)
114 RETURN_VALUE

116 RERAISE 0
118 COPY 3
120 POP_EXCEPT
122 RERAISE 1


0 NOP

2 LOAD_GLOBAL 1 (NULL + filedialog)
4 LOAD_ATTR 1 (askopenfilename)

6 LOAD_CONST 1 ("Pilih file .txt berisi prompts (satu per baris)")
8 LOAD_CONST 2 (('Text files', '*.txt'))
10 LOAD_CONST 3 (('All files', '*.*'))
12 BUILD_LIST 2

14 KW_NAMES 4 (('title', 'filetypes'))
16 CALL 2
18 STORE_FAST 1 (filename)

20 LOAD_FAST 1 (filename)
22 POP_JUMP_FORWARD_IF_FALSE 173 (to 126)

24 LOAD_GLOBAL 5 (NULL + Path)
26 LOAD_FAST 1 (filename)
28 CALL 1
30 LOAD_METHOD 3 (read_text)
32 LOAD_CONST 5 ("utf-8")
34 KW_NAMES 6 (('encoding',))
36 CALL 1
38 STORE_FAST 2 (content)

40 LOAD_FAST 0 (self)
42 LOAD_ATTR 4 (prompts_text)
44 LOAD_METHOD 5 (delete)
46 LOAD_CONST 7 ("1.0")
48 LOAD_GLOBAL 12 (tk)
50 LOAD_ATTR 7 (END)
52 CALL 2
54 POP_TOP

56 LOAD_FAST 0 (self)
58 LOAD_ATTR 4 (prompts_text)
60 LOAD_METHOD 8 (insert)
62 LOAD_GLOBAL 12 (tk)
64 LOAD_ATTR 7 (END)
66 LOAD_FAST 2 (content)
68 CALL 2
70 POP_TOP

72 LOAD_FAST 0 (self)
74 LOAD_METHOD 9 (_log)
76 LOAD_CONST 8 ("📄 Prompts dimuat dari: ")
78 LOAD_FAST 1 (filename)
80 FORMAT_VALUE 0
82 BUILD_STRING 2
84 CALL 1
86 POP_TOP

88 NOP

90 LOAD_FAST 0 (self)
92 LOAD_METHOD 10 (_update_prompt_count)
94 CALL 0
96 POP_TOP
98 LOAD_CONST 0 (None)
100 RETURN_VALUE
102 PUSH_EXC_INFO

104 LOAD_GLOBAL 22 (Exception)
106 CHECK_EXC_MATCH
108 POP_JUMP_FORWARD_IF_FALSE 4 (to 118)
110 POP_TOP

112 POP_EXCEPT
114 LOAD_CONST 0 (None)
116 RETURN_VALUE

118 RERAISE 0
120 COPY 3
122 POP_EXCEPT
124 RERAISE 1

126 LOAD_CONST 0 (None)
128 RETURN_VALUE
130 PUSH_EXC_INFO

132 LOAD_GLOBAL 22 (Exception)
134 CHECK_EXC_MATCH
136 POP_JUMP_FORWARD_IF_FALSE 35 (to 176)
138 STORE_FAST 3 (e)

140 LOAD_FAST 0 (self)
142 LOAD_METHOD 9 (_log)
144 LOAD_CONST 9 ("❌ Gagal load prompts: ")
146 LOAD_FAST 3 (e)
148 FORMAT_VALUE 0
150 BUILD_STRING 2
152 CALL 1
154 POP_TOP
156 POP_EXCEPT
158 LOAD_CONST 0 (None)
160 STORE_FAST 3 (e)
162 DELETE_FAST 3 (e)
164 LOAD_CONST 0 (None)
166 RETURN_VALUE
168 LOAD_CONST 0 (None)
170 STORE_FAST 3 (e)
172 DELETE_FAST 3 (e)
174 RERAISE 1

176 RERAISE 0
178 COPY 3
180 POP_EXCEPT
182 RERAISE 1


0 NOP

2 LOAD_GLOBAL 1 (NULL + filedialog)
4 LOAD_ATTR 1 (askdirectory)
6 LOAD_CONST 1 ("Pilih folder output")
8 KW_NAMES 2 (('title',))
10 CALL 1
12 STORE_FAST 1 (folder)

14 LOAD_FAST 1 (folder)
16 POP_JUMP_FORWARD_IF_FALSE 28 (to 34)

18 LOAD_FAST 0 (self)
20 LOAD_ATTR 2 (output_dir_var)
22 LOAD_METHOD 3 (set)
24 LOAD_FAST 1 (folder)
26 CALL 1
28 POP_TOP
30 LOAD_CONST 0 (None)
32 RETURN_VALUE

34 LOAD_CONST 0 (None)
36 RETURN_VALUE
38 PUSH_EXC_INFO

40 LOAD_GLOBAL 8 (Exception)
42 CHECK_EXC_MATCH
44 POP_JUMP_FORWARD_IF_FALSE 35 (to 84)
46 STORE_FAST 2 (e)

48 LOAD_FAST 0 (self)
50 LOAD_METHOD 5 (_log)
52 LOAD_CONST 3 ("❌ Gagal memilih folder output: ")
54 LOAD_FAST 2 (e)
56 FORMAT_VALUE 0
58 BUILD_STRING 2
60 CALL 1
62 POP_TOP
64 POP_EXCEPT
66 LOAD_CONST 0 (None)
68 STORE_FAST 2 (e)
70 DELETE_FAST 2 (e)
72 LOAD_CONST 0 (None)
74 RETURN_VALUE
76 LOAD_CONST 0 (None)
78 STORE_FAST 2 (e)
80 DELETE_FAST 2 (e)
82 RERAISE 1

84 RERAISE 0
86 COPY 3
88 POP_EXCEPT
90 RERAISE 1


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_METHOD 0 (_update_prompt_count)
6 CALL 0
8 POP_TOP
10 JUMP_FORWARD 16 (to 34)
12 PUSH_EXC_INFO

14 LOAD_GLOBAL 2 (Exception)
16 CHECK_EXC_MATCH
18 POP_JUMP_FORWARD_IF_FALSE 3 (to 26)
20 POP_TOP

22 POP_EXCEPT
24 JUMP_FORWARD 4 (to 34)

26 RERAISE 0
28 COPY 3
30 POP_EXCEPT
32 RERAISE 1

34 LOAD_FAST 0 (self)
36 LOAD_METHOD 2 (_collect_prompts)
38 CALL 0
40 STORE_FAST 1 (prompts)

42 LOAD_FAST 1 (prompts)
44 POP_JUMP_FORWARD_IF_TRUE 23 (to 62)

46 LOAD_GLOBAL 7 (NULL + messagebox)
48 LOAD_ATTR 4 (showwarning)
50 LOAD_CONST 1 ("Video Generator")
52 LOAD_CONST 2 ("Masukkan minimal satu prompt.")
54 CALL 2
56 POP_TOP

58 LOAD_CONST 0 (None)
60 RETURN_VALUE

62 LOAD_FAST 0 (self)
64 LOAD_ATTR 5 (api_key_var)
66 LOAD_METHOD 6 (get)
68 CALL 0
70 JUMP_IF_TRUE_OR_POP 1 (to 74)
72 LOAD_CONST 3 ("")
74 LOAD_METHOD 7 (strip)
76 CALL 0
78 POP_JUMP_FORWARD_IF_TRUE 23 (to 96)

80 LOAD_GLOBAL 7 (NULL + messagebox)
82 LOAD_ATTR 4 (showwarning)
84 LOAD_CONST 1 ("Video Generator")
86 LOAD_CONST 4 ("API key belum tersedia. Silakan jalankan proses create API key terlebih dahulu.")
88 CALL 2
90 POP_TOP

92 LOAD_CONST 0 (None)
94 RETURN_VALUE

96 LOAD_FAST 0 (self)
98 LOAD_ATTR 8 (output_dir_var)
100 LOAD_METHOD 6 (get)
102 CALL 0
104 JUMP_IF_TRUE_OR_POP 1 (to 108)
106 LOAD_CONST 3 ("")
108 LOAD_METHOD 7 (strip)
110 CALL 0
112 STORE_FAST 2 (out_dir)

114 LOAD_FAST 2 (out_dir)
116 POP_JUMP_FORWARD_IF_TRUE 23 (to 134)

118 LOAD_GLOBAL 7 (NULL + messagebox)
120 LOAD_ATTR 4 (showwarning)
122 LOAD_CONST 1 ("Video Generator")
124 LOAD_CONST 5 ("Pilih folder output terlebih dahulu.")
126 CALL 2
128 POP_TOP

130 LOAD_CONST 0 (None)
132 RETURN_VALUE

134 LOAD_GLOBAL 19 (NULL + Path)
136 LOAD_FAST 2 (out_dir)
138 CALL 1
140 LOAD_METHOD 10 (mkdir)
142 LOAD_CONST 6 (True)
144 LOAD_CONST 6 (True)
146 KW_NAMES 7 (('parents', 'exist_ok'))
148 CALL 2
150 POP_TOP

152 LOAD_FAST 0 (self)
154 LOAD_ATTR 11 (model_var)
156 LOAD_METHOD 6 (get)
158 CALL 0
160 JUMP_IF_TRUE_OR_POP 1 (to 164)
162 LOAD_CONST 3 ("")
164 LOAD_METHOD 7 (strip)
166 CALL 0
168 STORE_FAST 3 (model)

170 LOAD_FAST 0 (self)
172 LOAD_ATTR 12 (aspect_ratio_var)
174 LOAD_METHOD 6 (get)
176 CALL 0
178 JUMP_IF_TRUE_OR_POP 1 (to 182)
180 LOAD_CONST 3 ("")
182 LOAD_METHOD 7 (strip)
184 CALL 0
186 STORE_FAST 4 (aspect)

188 LOAD_FAST 0 (self)
190 LOAD_ATTR 13 (neg_prompt_var)
192 LOAD_METHOD 6 (get)
194 CALL 0
196 JUMP_IF_TRUE_OR_POP 1 (to 200)
198 LOAD_CONST 3 ("")
200 LOAD_METHOD 7 (strip)
202 CALL 0
204 JUMP_IF_TRUE_OR_POP 1 (to 208)
206 LOAD_CONST 0 (None)
208 STORE_FAST 5 (neg)

210 LOAD_GLOBAL 29 (NULL + bool)
212 LOAD_FAST 0 (self)
214 LOAD_ATTR 15 (image_to_video_var)
216 LOAD_METHOD 6 (get)
218 CALL 0
220 CALL 1
222 STORE_FAST 6 (img2vid)

224 LOAD_GLOBAL 29 (NULL + bool)
226 LOAD_FAST 0 (self)
228 LOAD_ATTR 16 (veo2_double_var)
230 LOAD_METHOD 6 (get)
232 CALL 0
234 CALL 1
236 JUMP_IF_FALSE_OR_POP 20 (to 246)
238 LOAD_FAST 3 (model)
240 LOAD_METHOD 17 (startswith)
242 LOAD_CONST 8 ("veo-2")
244 CALL 1
246 STORE_FAST 7 (veo2_double)

248 LOAD_GLOBAL 29 (NULL + bool)
250 LOAD_FAST 0 (self)
252 LOAD_ATTR 18 (veo3_audio_var)
254 LOAD_METHOD 6 (get)
256 CALL 0
258 CALL 1
260 JUMP_IF_FALSE_OR_POP 20 (to 270)
262 LOAD_FAST 3 (model)
264 LOAD_METHOD 17 (startswith)
266 LOAD_CONST 9 ("veo-3")
268 CALL 1
270 STORE_FAST 8 (veo3_audio)

272 LOAD_FAST 3 (model)
274 LOAD_METHOD 17 (startswith)
276 LOAD_CONST 9 ("veo-3")
278 CALL 1
280 POP_JUMP_FORWARD_IF_FALSE 47 (to 304)
282 LOAD_FAST 0 (self)
284 LOAD_ATTR 19 (resolution_var)
286 LOAD_METHOD 6 (get)
288 CALL 0
290 JUMP_IF_TRUE_OR_POP 1 (to 294)
292 LOAD_CONST 3 ("")
294 LOAD_METHOD 7 (strip)
296 CALL 0
298 JUMP_IF_TRUE_OR_POP 1 (to 302)
300 LOAD_CONST 0 (None)
302 JUMP_FORWARD 1 (to 306)
304 LOAD_CONST 0 (None)
306 STORE_FAST 9 (resolution)

308 LOAD_FAST 0 (self)
310 LOAD_ATTR 20 (start_btn)
312 LOAD_METHOD 21 (configure)
314 LOAD_GLOBAL 44 (DISABLED)
316 KW_NAMES 10 (('state',))
318 CALL 1
320 POP_TOP

322 NOP

324 LOAD_FAST 0 (self)
326 LOAD_ATTR 23 (stop_btn)
328 LOAD_METHOD 21 (configure)
330 LOAD_GLOBAL 48 (NORMAL)
332 KW_NAMES 10 (('state',))
334 CALL 1
336 POP_TOP
338 JUMP_FORWARD 16 (to 362)
340 PUSH_EXC_INFO

342 LOAD_GLOBAL 2 (Exception)
344 CHECK_EXC_MATCH
346 POP_JUMP_FORWARD_IF_FALSE 3 (to 354)
348 POP_TOP

350 POP_EXCEPT
352 JUMP_FORWARD 4 (to 362)

354 RERAISE 0
356 COPY 3
358 POP_EXCEPT
360 RERAISE 1

362 LOAD_GLOBAL 51 (NULL + threading)
364 LOAD_ATTR 26 (Event)
366 CALL 0
368 LOAD_FAST 0 (self)
370 STORE_ATTR 27 (_stop_event)

372 LOAD_GLOBAL 51 (NULL + threading)
374 LOAD_ATTR 28 (Thread)

376 LOAD_FAST 0 (self)
378 LOAD_ATTR 29 (_worker_generate)

380 LOAD_FAST 1 (prompts)
382 LOAD_FAST 2 (out_dir)
384 LOAD_FAST 3 (model)
386 LOAD_FAST 4 (aspect)
388 LOAD_FAST 5 (neg)
390 LOAD_FAST 6 (img2vid)
392 LOAD_FAST 7 (veo2_double)
394 LOAD_FAST 8 (veo3_audio)
396 LOAD_FAST 9 (resolution)
398 BUILD_TUPLE 9

400 LOAD_CONST 6 (True)

402 KW_NAMES 11 (('target', 'args', 'daemon'))
404 CALL 3
406 STORE_FAST 10 (t)

408 LOAD_FAST 10 (t)
410 LOAD_FAST 0 (self)
412 STORE_ATTR 30 (_worker_thread)

414 LOAD_FAST 10 (t)
416 LOAD_METHOD 31 (start)
418 CALL 0
420 POP_TOP
422 LOAD_CONST 0 (None)
424 RETURN_VALUE


0 NOP

2 LOAD_GLOBAL 1 (NULL + GenAIVideoService)
4 LOAD_DEREF 0 (self)
6 LOAD_ATTR 1 (api_key_var)
8 LOAD_METHOD 2 (get)
10 CALL 0
12 JUMP_IF_TRUE_OR_POP 1 (to 16)
14 LOAD_CONST 1 ("")
16 LOAD_METHOD 3 (strip)
18 CALL 0
20 KW_NAMES 2 (('api_key',))
22 CALL 1
24 STORE_FAST 10 (svc)

26 LOAD_GLOBAL 9 (NULL + VideoPostprocessService)
28 CALL 0
30 STORE_FAST 11 (post)

32 LOAD_GLOBAL 11 (NULL + len)
34 LOAD_FAST 1 (prompts)
36 CALL 1
38 STORE_FAST 12 (total)

40 LOAD_DEREF 0 (self)
42 LOAD_METHOD 6 (_set_progress)
44 LOAD_CONST 3 ("Mulai generate ")
46 LOAD_FAST 12 (total)
48 FORMAT_VALUE 0
50 LOAD_CONST 4 (" prompt...")
52 BUILD_STRING 3
54 CALL 1
56 POP_TOP

58 LOAD_GLOBAL 15 (NULL + enumerate)
60 LOAD_FAST 1 (prompts)
62 LOAD_CONST 5 (1)
64 KW_NAMES 6 (('start',))
66 CALL 2
68 GET_ITER
70 FOR_ITER 1867 (to 1448)
72 UNPACK_SEQUENCE 2
74 STORE_FAST 13 (idx)
76 STORE_FAST 14 (prompt)

78 LOAD_DEREF 0 (self)
80 LOAD_ATTR 8 (_stop_event)
82 POP_JUMP_FORWARD_IF_FALSE 184 (to 210)
84 LOAD_DEREF 0 (self)
86 LOAD_ATTR 8 (_stop_event)
88 LOAD_METHOD 9 (is_set)
90 CALL 0
92 POP_JUMP_FORWARD_IF_FALSE 159 (to 210)

94 LOAD_DEREF 0 (self)
96 LOAD_METHOD 10 (_log)
98 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
100 CALL 1
102 POP_TOP

104 POP_TOP

106 LOAD_DEREF 0 (self)
108 LOAD_ATTR 11 (root)
110 LOAD_METHOD 12 (after)
112 LOAD_CONST 8 (0)
114 LOAD_CLOSURE 0 (self)
116 BUILD_TUPLE 1
118 LOAD_CONST 9 (code object <lambda>)
120 MAKE_FUNCTION 8 (closure)
122 CALL 2
124 POP_TOP

126 NOP

128 LOAD_DEREF 0 (self)
130 LOAD_ATTR 11 (root)
132 LOAD_METHOD 12 (after)
134 LOAD_CONST 8 (0)
136 LOAD_CLOSURE 0 (self)
138 BUILD_TUPLE 1
140 LOAD_CONST 10 (code object <lambda>)
142 MAKE_FUNCTION 8 (closure)
144 CALL 2
146 POP_TOP
148 JUMP_FORWARD 16 (to 172)
150 PUSH_EXC_INFO

152 LOAD_GLOBAL 26 (Exception)
154 CHECK_EXC_MATCH
156 POP_JUMP_FORWARD_IF_FALSE 3 (to 164)
158 POP_TOP

160 POP_EXCEPT
162 JUMP_FORWARD 4 (to 172)

164 RERAISE 0
166 COPY 3
168 POP_EXCEPT
170 RERAISE 1

172 LOAD_DEREF 0 (self)
174 LOAD_ATTR 8 (_stop_event)
176 POP_JUMP_FORWARD_IF_FALSE 48 (to 202)
178 LOAD_DEREF 0 (self)
180 LOAD_ATTR 8 (_stop_event)
182 LOAD_METHOD 9 (is_set)
184 CALL 0
186 POP_JUMP_FORWARD_IF_FALSE 25 (to 206)

188 LOAD_DEREF 0 (self)
190 LOAD_METHOD 6 (_set_progress)
192 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
194 CALL 1
196 POP_TOP
198 LOAD_CONST 0 (None)
200 RETURN_VALUE

202 LOAD_CONST 0 (None)
204 RETURN_VALUE
206 LOAD_CONST 0 (None)
208 RETURN_VALUE

210 LOAD_DEREF 0 (self)
212 LOAD_METHOD 6 (_set_progress)
214 LOAD_CONST 12 ("[")
216 LOAD_FAST 13 (idx)
218 FORMAT_VALUE 0
220 LOAD_CONST 13 ("/")
222 LOAD_FAST 12 (total)
224 FORMAT_VALUE 0
226 LOAD_CONST 14 ("] Generating...")
228 BUILD_STRING 5
230 CALL 1
232 POP_TOP

234 LOAD_CONST 15 (False)
236 STORE_FAST 15 (retried)

238 NOP

240 LOAD_DEREF 0 (self)
242 LOAD_ATTR 8 (_stop_event)
244 POP_JUMP_FORWARD_IF_FALSE 184 (to 372)
246 LOAD_DEREF 0 (self)
248 LOAD_ATTR 8 (_stop_event)
250 LOAD_METHOD 9 (is_set)
252 CALL 0
254 POP_JUMP_FORWARD_IF_FALSE 159 (to 372)

256 LOAD_DEREF 0 (self)
258 LOAD_METHOD 10 (_log)
260 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
262 CALL 1
264 POP_TOP

266 POP_TOP

268 LOAD_DEREF 0 (self)
270 LOAD_ATTR 11 (root)
272 LOAD_METHOD 12 (after)
274 LOAD_CONST 8 (0)
276 LOAD_CLOSURE 0 (self)
278 BUILD_TUPLE 1
280 LOAD_CONST 9 (code object <lambda>)
282 MAKE_FUNCTION 8 (closure)
284 CALL 2
286 POP_TOP

288 NOP

290 LOAD_DEREF 0 (self)
292 LOAD_ATTR 11 (root)
294 LOAD_METHOD 12 (after)
296 LOAD_CONST 8 (0)
298 LOAD_CLOSURE 0 (self)
300 BUILD_TUPLE 1
302 LOAD_CONST 10 (code object <lambda>)
304 MAKE_FUNCTION 8 (closure)
306 CALL 2
308 POP_TOP
310 JUMP_FORWARD 16 (to 334)
312 PUSH_EXC_INFO

314 LOAD_GLOBAL 26 (Exception)
316 CHECK_EXC_MATCH
318 POP_JUMP_FORWARD_IF_FALSE 3 (to 326)
320 POP_TOP

322 POP_EXCEPT
324 JUMP_FORWARD 4 (to 334)

326 RERAISE 0
328 COPY 3
330 POP_EXCEPT
332 RERAISE 1

334 LOAD_DEREF 0 (self)
336 LOAD_ATTR 8 (_stop_event)
338 POP_JUMP_FORWARD_IF_FALSE 48 (to 364)
340 LOAD_DEREF 0 (self)
342 LOAD_ATTR 8 (_stop_event)
344 LOAD_METHOD 9 (is_set)
346 CALL 0
348 POP_JUMP_FORWARD_IF_FALSE 25 (to 368)

350 LOAD_DEREF 0 (self)
352 LOAD_METHOD 6 (_set_progress)
354 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
356 CALL 1
358 POP_TOP
360 LOAD_CONST 0 (None)
362 RETURN_VALUE

364 LOAD_CONST 0 (None)
366 RETURN_VALUE
368 LOAD_CONST 0 (None)
370 RETURN_VALUE

372 NOP

374 LOAD_CONST 0 (None)
376 STORE_FAST 16 (image)

378 LOAD_FAST 6 (img2vid)
380 POP_JUMP_FORWARD_IF_FALSE 235 (to 538)

382 LOAD_DEREF 0 (self)
384 LOAD_ATTR 8 (_stop_event)
386 POP_JUMP_FORWARD_IF_FALSE 184 (to 514)
388 LOAD_DEREF 0 (self)
390 LOAD_ATTR 8 (_stop_event)
392 LOAD_METHOD 9 (is_set)
394 CALL 0
396 POP_JUMP_FORWARD_IF_FALSE 159 (to 514)

398 LOAD_DEREF 0 (self)
400 LOAD_METHOD 10 (_log)
402 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
404 CALL 1
406 POP_TOP

408 POP_TOP

410 LOAD_DEREF 0 (self)
412 LOAD_ATTR 11 (root)
414 LOAD_METHOD 12 (after)
416 LOAD_CONST 8 (0)
418 LOAD_CLOSURE 0 (self)
420 BUILD_TUPLE 1
422 LOAD_CONST 9 (code object <lambda>)
424 MAKE_FUNCTION 8 (closure)
426 CALL 2
428 POP_TOP

430 NOP

432 LOAD_DEREF 0 (self)
434 LOAD_ATTR 11 (root)
436 LOAD_METHOD 12 (after)
438 LOAD_CONST 8 (0)
440 LOAD_CLOSURE 0 (self)
442 BUILD_TUPLE 1
444 LOAD_CONST 10 (code object <lambda>)
446 MAKE_FUNCTION 8 (closure)
448 CALL 2
450 POP_TOP
452 JUMP_FORWARD 16 (to 476)
454 PUSH_EXC_INFO

456 LOAD_GLOBAL 26 (Exception)
458 CHECK_EXC_MATCH
460 POP_JUMP_FORWARD_IF_FALSE 3 (to 468)
462 POP_TOP

464 POP_EXCEPT
466 JUMP_FORWARD 4 (to 476)

468 RERAISE 0
470 COPY 3
472 POP_EXCEPT
474 RERAISE 1

476 LOAD_DEREF 0 (self)
478 LOAD_ATTR 8 (_stop_event)
480 POP_JUMP_FORWARD_IF_FALSE 48 (to 506)
482 LOAD_DEREF 0 (self)
484 LOAD_ATTR 8 (_stop_event)
486 LOAD_METHOD 9 (is_set)
488 CALL 0
490 POP_JUMP_FORWARD_IF_FALSE 25 (to 510)

492 LOAD_DEREF 0 (self)
494 LOAD_METHOD 6 (_set_progress)
496 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
498 CALL 1
500 POP_TOP
502 LOAD_CONST 0 (None)
504 RETURN_VALUE

506 LOAD_CONST 0 (None)
508 RETURN_VALUE
510 LOAD_CONST 0 (None)
512 RETURN_VALUE

514 LOAD_DEREF 0 (self)
516 LOAD_METHOD 10 (_log)
518 LOAD_CONST 17 ("🖼️ Generating image via Imagen 4 Ultra...")
520 CALL 1
522 POP_TOP

524 LOAD_FAST 10 (svc)
526 LOAD_METHOD 14 (generate_image_with_imagen)
528 LOAD_FAST 14 (prompt)
530 LOAD_CONST 18 ("imagen-4.0-generate-001")
532 KW_NAMES 19 (('prompt', 'imagen_model'))
534 CALL 2
536 STORE_FAST 16 (image)

538 LOAD_FAST 7 (veo2_double)
540 POP_JUMP_FORWARD_IF_FALSE 2 (to 546)
542 LOAD_CONST 20 (2)
544 JUMP_FORWARD 1 (to 548)
546 LOAD_CONST 5 (1)
548 STORE_FAST 17 (runs)

550 BUILD_LIST 0
552 STORE_FAST 18 (saved_paths)

554 LOAD_GLOBAL 31 (NULL + range)
556 LOAD_CONST 5 (1)
558 LOAD_FAST 17 (runs)
560 LOAD_CONST 5 (1)
562 BINARY_OP 0
564 CALL 2
566 GET_ITER
568 FOR_ITER 939 (to 1240)
570 STORE_FAST 19 (r)

572 LOAD_DEREF 0 (self)
574 LOAD_ATTR 8 (_stop_event)
576 POP_JUMP_FORWARD_IF_FALSE 185 (to 706)
578 LOAD_DEREF 0 (self)
580 LOAD_ATTR 8 (_stop_event)
582 LOAD_METHOD 9 (is_set)
584 CALL 0
586 POP_JUMP_FORWARD_IF_FALSE 160 (to 706)

588 LOAD_DEREF 0 (self)
590 LOAD_METHOD 10 (_log)
592 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
594 CALL 1
596 POP_TOP

598 POP_TOP
600 POP_TOP

602 LOAD_DEREF 0 (self)
604 LOAD_ATTR 11 (root)
606 LOAD_METHOD 12 (after)
608 LOAD_CONST 8 (0)
610 LOAD_CLOSURE 0 (self)
612 BUILD_TUPLE 1
614 LOAD_CONST 9 (code object <lambda>)
616 MAKE_FUNCTION 8 (closure)
618 CALL 2
620 POP_TOP

622 NOP

624 LOAD_DEREF 0 (self)
626 LOAD_ATTR 11 (root)
628 LOAD_METHOD 12 (after)
630 LOAD_CONST 8 (0)
632 LOAD_CLOSURE 0 (self)
634 BUILD_TUPLE 1
636 LOAD_CONST 10 (code object <lambda>)
638 MAKE_FUNCTION 8 (closure)
640 CALL 2
642 POP_TOP
644 JUMP_FORWARD 16 (to 668)
646 PUSH_EXC_INFO

648 LOAD_GLOBAL 26 (Exception)
650 CHECK_EXC_MATCH
652 POP_JUMP_FORWARD_IF_FALSE 3 (to 660)
654 POP_TOP

656 POP_EXCEPT
658 JUMP_FORWARD 4 (to 668)

660 RERAISE 0
662 COPY 3
664 POP_EXCEPT
666 RERAISE 1

668 LOAD_DEREF 0 (self)
670 LOAD_ATTR 8 (_stop_event)
672 POP_JUMP_FORWARD_IF_FALSE 48 (to 698)
674 LOAD_DEREF 0 (self)
676 LOAD_ATTR 8 (_stop_event)
678 LOAD_METHOD 9 (is_set)
680 CALL 0
682 POP_JUMP_FORWARD_IF_FALSE 25 (to 702)

684 LOAD_DEREF 0 (self)
686 LOAD_METHOD 6 (_set_progress)
688 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
690 CALL 1
692 POP_TOP
694 LOAD_CONST 0 (None)
696 RETURN_VALUE

698 LOAD_CONST 0 (None)
700 RETURN_VALUE
702 LOAD_CONST 0 (None)
704 RETURN_VALUE

706 LOAD_FAST 10 (svc)
708 LOAD_METHOD 16 (generate_video)

710 LOAD_FAST 14 (prompt)

712 LOAD_FAST 3 (model)

714 LOAD_FAST 4 (aspect)
716 JUMP_IF_TRUE_OR_POP 1 (to 720)
718 LOAD_CONST 0 (None)

720 LOAD_FAST 5 (neg)

722 LOAD_FAST 16 (image)

724 LOAD_FAST 9 (resolution)

726 KW_NAMES 21 (('prompt', 'model', 'aspect_ratio', 'negative_prompt', 'image', 'resolution'))
728 CALL 6
730 STORE_FAST 20 (resp)

732 LOAD_FAST 20 (resp)
734 LOAD_METHOD 2 (get)
736 LOAD_CONST 22 ("generated_videos")
738 CALL 1
740 JUMP_IF_TRUE_OR_POP 1 (to 744)
742 BUILD_LIST 0
744 STORE_FAST 21 (gen_videos)

746 LOAD_FAST 21 (gen_videos)
748 POP_JUMP_FORWARD_IF_TRUE 15 (to 758)

750 LOAD_GLOBAL 35 (NULL + RuntimeError)
752 LOAD_CONST 23 ("Tidak ada video pada response.")
754 CALL 1
756 RAISE_VARARGS 1 (exception instance)

758 LOAD_DEREF 0 (self)
760 LOAD_METHOD 18 (_safe_name)
762 LOAD_FAST 14 (prompt)
764 CALL 1
766 LOAD_CONST 0 (None)
768 LOAD_CONST 24 (40)
770 BUILD_SLICE 2
772 BINARY_SUBSCR
774 JUMP_IF_TRUE_OR_POP 1 (to 778)
776 LOAD_CONST 25 ("video")
778 STORE_DEREF 27 (self)

780 LOAD_GLOBAL 39 (NULL + datetime)
782 LOAD_ATTR 20 (now)
784 CALL 0
786 LOAD_METHOD 21 (strftime)
788 LOAD_CONST 26 ("%Y%m%d_%H%M%S")
790 CALL 1
792 STORE_DEREF 29 (base)

794 LOAD_FAST 17 (runs)
796 LOAD_CONST 5 (1)
798 COMPARE_OP 4 (>)
800 POP_JUMP_FORWARD_IF_FALSE 5 (to 812)
802 LOAD_CONST 27 ("_")
804 LOAD_FAST 19 (r)
806 FORMAT_VALUE 0
808 BUILD_STRING 2
810 JUMP_FORWARD 1 (to 814)
812 LOAD_CONST 1 ("")
814 STORE_DEREF 28 (out_dir)

816 LOAD_CLOSURE 27 (self)
818 LOAD_CLOSURE 2 (out_dir)
820 LOAD_CLOSURE 28 (out_dir)
822 LOAD_CLOSURE 29 (base)
824 BUILD_TUPLE 4
826 LOAD_CONST 28 (code object <listcomp>)
828 MAKE_FUNCTION 8 (closure)
830 LOAD_GLOBAL 31 (NULL + range)
832 LOAD_GLOBAL 11 (NULL + len)
834 LOAD_FAST 21 (gen_videos)
836 CALL 1
838 CALL 1
840 GET_ITER
842 CALL 0
844 STORE_FAST 22 (paths)

846 LOAD_DEREF 0 (self)
848 LOAD_ATTR 8 (_stop_event)
850 POP_JUMP_FORWARD_IF_FALSE 185 (to 980)
852 LOAD_DEREF 0 (self)
854 LOAD_ATTR 8 (_stop_event)
856 LOAD_METHOD 9 (is_set)
858 CALL 0
860 POP_JUMP_FORWARD_IF_FALSE 160 (to 980)

862 LOAD_DEREF 0 (self)
864 LOAD_METHOD 10 (_log)
866 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
868 CALL 1
870 POP_TOP

872 POP_TOP
874 POP_TOP

876 LOAD_DEREF 0 (self)
878 LOAD_ATTR 11 (root)
880 LOAD_METHOD 12 (after)
882 LOAD_CONST 8 (0)
884 LOAD_CLOSURE 0 (self)
886 BUILD_TUPLE 1
888 LOAD_CONST 9 (code object <lambda>)
890 MAKE_FUNCTION 8 (closure)
892 CALL 2
894 POP_TOP

896 NOP

898 LOAD_DEREF 0 (self)
900 LOAD_ATTR 11 (root)
902 LOAD_METHOD 12 (after)
904 LOAD_CONST 8 (0)
906 LOAD_CLOSURE 0 (self)
908 BUILD_TUPLE 1
910 LOAD_CONST 10 (code object <lambda>)
912 MAKE_FUNCTION 8 (closure)
914 CALL 2
916 POP_TOP
918 JUMP_FORWARD 16 (to 942)
920 PUSH_EXC_INFO

922 LOAD_GLOBAL 26 (Exception)
924 CHECK_EXC_MATCH
926 POP_JUMP_FORWARD_IF_FALSE 3 (to 934)
928 POP_TOP

930 POP_EXCEPT
932 JUMP_FORWARD 4 (to 942)

934 RERAISE 0
936 COPY 3
938 POP_EXCEPT
940 RERAISE 1

942 LOAD_DEREF 0 (self)
944 LOAD_ATTR 8 (_stop_event)
946 POP_JUMP_FORWARD_IF_FALSE 48 (to 972)
948 LOAD_DEREF 0 (self)
950 LOAD_ATTR 8 (_stop_event)
952 LOAD_METHOD 9 (is_set)
954 CALL 0
956 POP_JUMP_FORWARD_IF_FALSE 25 (to 976)

958 LOAD_DEREF 0 (self)
960 LOAD_METHOD 6 (_set_progress)
962 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
964 CALL 1
966 POP_TOP
968 LOAD_CONST 0 (None)
970 RETURN_VALUE

972 LOAD_CONST 0 (None)
974 RETURN_VALUE
976 LOAD_CONST 0 (None)
978 RETURN_VALUE

980 LOAD_FAST 10 (svc)
982 LOAD_METHOD 22 (download_videos)
984 LOAD_FAST 21 (gen_videos)
986 LOAD_FAST 22 (paths)
988 CALL 2
990 POP_TOP

992 LOAD_FAST 18 (saved_paths)
994 LOAD_METHOD 23 (extend)
996 LOAD_FAST 22 (paths)
998 LOAD_CONST 0 (None)
1000 LOAD_GLOBAL 11 (NULL + len)
1002 LOAD_FAST 21 (gen_videos)
1004 CALL 1
1006 BUILD_SLICE 2
1008 BINARY_SUBSCR
1010 CALL 1
1012 POP_TOP

1014 LOAD_FAST 8 (veo3_audio)
1016 POP_JUMP_FORWARD_IF_TRUE 291 (to 1238)
1018 LOAD_FAST 3 (model)
1020 LOAD_METHOD 24 (startswith)
1022 LOAD_CONST 29 ("veo-3")
1024 CALL 1
1026 POP_JUMP_FORWARD_IF_FALSE 269 (to 1238)

1028 LOAD_FAST 22 (paths)
1030 GET_ITER
1032 FOR_ITER 265 (to 1238)
1034 STORE_FAST 23 (p)

1036 LOAD_DEREF 0 (self)
1038 LOAD_ATTR 8 (_stop_event)
1040 POP_JUMP_FORWARD_IF_FALSE 186 (to 1172)
1042 LOAD_DEREF 0 (self)
1044 LOAD_ATTR 8 (_stop_event)
1046 LOAD_METHOD 9 (is_set)
1048 CALL 0
1050 POP_JUMP_FORWARD_IF_FALSE 161 (to 1172)

1052 LOAD_DEREF 0 (self)
1054 LOAD_METHOD 10 (_log)
1056 LOAD_CONST 7 ("⏹️ Dihentikan oleh pengguna.")
1058 CALL 1
1060 POP_TOP

1062 POP_TOP
1064 POP_TOP
1066 POP_TOP

1068 LOAD_DEREF 0 (self)
1070 LOAD_ATTR 11 (root)
1072 LOAD_METHOD 12 (after)
1074 LOAD_CONST 8 (0)
1076 LOAD_CLOSURE 0 (self)
1078 BUILD_TUPLE 1
1080 LOAD_CONST 9 (code object <lambda>)
1082 MAKE_FUNCTION 8 (closure)
1084 CALL 2
1086 POP_TOP

1088 NOP

1090 LOAD_DEREF 0 (self)
1092 LOAD_ATTR 11 (root)
1094 LOAD_METHOD 12 (after)
1096 LOAD_CONST 8 (0)
1098 LOAD_CLOSURE 0 (self)
1100 BUILD_TUPLE 1
1102 LOAD_CONST 10 (code object <lambda>)
1104 MAKE_FUNCTION 8 (closure)
1106 CALL 2
1108 POP_TOP
1110 JUMP_FORWARD 16 (to 1134)
1112 PUSH_EXC_INFO

1114 LOAD_GLOBAL 26 (Exception)
1116 CHECK_EXC_MATCH
1118 POP_JUMP_FORWARD_IF_FALSE 3 (to 1126)
1120 POP_TOP

1122 POP_EXCEPT
1124 JUMP_FORWARD 4 (to 1134)

1126 RERAISE 0
1128 COPY 3
1130 POP_EXCEPT
1132 RERAISE 1

1134 LOAD_DEREF 0 (self)
1136 LOAD_ATTR 8 (_stop_event)
1138 POP_JUMP_FORWARD_IF_FALSE 48 (to 1164)
1140 LOAD_DEREF 0 (self)
1142 LOAD_ATTR 8 (_stop_event)
1144 LOAD_METHOD 9 (is_set)
1146 CALL 0
1148 POP_JUMP_FORWARD_IF_FALSE 25 (to 1168)

1150 LOAD_DEREF 0 (self)
1152 LOAD_METHOD 6 (_set_progress)
1154 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
1156 CALL 1
1158 POP_TOP
1160 LOAD_CONST 0 (None)
1162 RETURN_VALUE

1164 LOAD_CONST 0 (None)
1166 RETURN_VALUE
1168 LOAD_CONST 0 (None)
1170 RETURN_VALUE

1172 NOP

1174 LOAD_FAST 11 (post)
1176 LOAD_METHOD 25 (remove_audio_inplace)
1178 LOAD_FAST 23 (p)
1180 CALL 1
1182 POP_TOP
1184 JUMP_BACKWARD 219 (to 1032)
1186 PUSH_EXC_INFO

1188 LOAD_GLOBAL 26 (Exception)
1190 CHECK_EXC_MATCH
1192 POP_JUMP_FORWARD_IF_FALSE 35 (to 1230)
1194 STORE_FAST 24 (e)

1196 LOAD_DEREF 0 (self)
1198 LOAD_METHOD 10 (_log)
1200 LOAD_CONST 30 ("⚠️ Gagal hapus audio: ")
1202 LOAD_FAST 24 (e)
1204 FORMAT_VALUE 0
1206 BUILD_STRING 2
1208 CALL 1
1210 POP_TOP
1212 POP_EXCEPT
1214 LOAD_CONST 0 (None)
1216 STORE_FAST 24 (e)
1218 DELETE_FAST 24 (e)
1220 JUMP_BACKWARD 259 (to 1032)
1222 LOAD_CONST 0 (None)
1224 STORE_FAST 24 (e)
1226 DELETE_FAST 24 (e)
1228 RERAISE 1

1230 RERAISE 0
1232 COPY 3
1234 POP_EXCEPT
1236 RERAISE 1
1238 JUMP_BACKWARD 941 (to 568)

1240 LOAD_DEREF 0 (self)
1242 LOAD_METHOD 10 (_log)
1244 LOAD_CONST 31 ("✅ Selesai prompt ")
1246 LOAD_FAST 13 (idx)
1248 FORMAT_VALUE 0
1250 LOAD_CONST 13 ("/")
1252 LOAD_FAST 12 (total)
1254 FORMAT_VALUE 0
1256 LOAD_CONST 32 (". Files: ")
1258 LOAD_FAST 18 (saved_paths)
1260 FORMAT_VALUE 0
1262 BUILD_STRING 6
1264 CALL 1
1266 POP_TOP

1268 JUMP_FORWARD 209 (to 1446)
1270 PUSH_EXC_INFO

1272 LOAD_GLOBAL 26 (Exception)
1274 CHECK_EXC_MATCH
1276 POP_JUMP_FORWARD_IF_FALSE 196 (to 1438)
1278 STORE_FAST 24 (e)

1280 LOAD_GLOBAL 53 (NULL + str)
1282 LOAD_FAST 24 (e)
1284 CALL 1
1286 STORE_FAST 25 (err_msg)

1288 LOAD_DEREF 0 (self)
1290 LOAD_METHOD 10 (_log)
1292 LOAD_CONST 33 ("❌ Gagal generate untuk prompt ke-")
1294 LOAD_FAST 13 (idx)
1296 FORMAT_VALUE 0
1298 LOAD_CONST 34 (": ")
1300 LOAD_FAST 24 (e)
1302 FORMAT_VALUE 0
1304 BUILD_STRING 4
1306 CALL 1
1308 POP_TOP

1310 LOAD_FAST 15 (retried)
1312 POP_JUMP_FORWARD_IF_TRUE 142 (to 1420)
1314 LOAD_DEREF 0 (self)
1316 LOAD_METHOD 27 (_needs_new_api_key)
1318 LOAD_FAST 25 (err_msg)
1320 CALL 1
1322 POP_JUMP_FORWARD_IF_FALSE 121 (to 1420)
1324 LOAD_DEREF 0 (self)
1326 LOAD_ATTR 28 (request_new_api_key_and_wait)
1328 POP_JUMP_FORWARD_IF_FALSE 114 (to 1420)

1330 LOAD_DEREF 0 (self)
1332 LOAD_METHOD 28 (request_new_api_key_and_wait)
1334 LOAD_FAST 25 (err_msg)
1336 LOAD_CONST 35 (900)
1338 KW_NAMES 36 (('reason', 'timeout_seconds'))
1340 CALL 2
1342 STORE_FAST 26 (new_key)

1344 LOAD_FAST 26 (new_key)
1346 POP_JUMP_FORWARD_IF_FALSE 89 (to 1420)

1348 NOP

1350 LOAD_DEREF 0 (self)
1352 LOAD_ATTR 1 (api_key_var)
1354 LOAD_METHOD 29 (set)
1356 LOAD_FAST 26 (new_key)
1358 CALL 1
1360 POP_TOP
1362 JUMP_FORWARD 16 (to 1386)
1364 PUSH_EXC_INFO

1366 LOAD_GLOBAL 26 (Exception)
1368 CHECK_EXC_MATCH
1370 POP_JUMP_FORWARD_IF_FALSE 3 (to 1378)
1372 POP_TOP

1374 POP_EXCEPT
1376 JUMP_FORWARD 4 (to 1386)

1378 RERAISE 0
1380 COPY 3
1382 POP_EXCEPT
1384 RERAISE 1

1386 LOAD_DEREF 0 (self)
1388 LOAD_METHOD 10 (_log)
1390 LOAD_CONST 37 ("🔑 API key baru diterima. Melanjutkan otomatis...")
1392 CALL 1
1394 POP_TOP

1396 LOAD_GLOBAL 1 (NULL + GenAIVideoService)
1398 LOAD_FAST 26 (new_key)
1400 KW_NAMES 2 (('api_key',))
1402 CALL 1
1404 STORE_FAST 10 (svc)

1406 LOAD_CONST 16 (True)
1408 STORE_FAST 15 (retried)

1410 POP_EXCEPT
1412 LOAD_CONST 0 (None)
1414 STORE_FAST 24 (e)
1416 DELETE_FAST 24 (e)
1418 JUMP_BACKWARD 1627 (to 238)

1420 POP_EXCEPT
1422 LOAD_CONST 0 (None)
1424 STORE_FAST 24 (e)
1426 DELETE_FAST 24 (e)
1428 JUMP_FORWARD 8 (to 1446)
1430 LOAD_CONST 0 (None)
1432 STORE_FAST 24 (e)
1434 DELETE_FAST 24 (e)
1436 RERAISE 1

1438 RERAISE 0
1440 COPY 3
1442 POP_EXCEPT
1444 RERAISE 1
1446 JUMP_BACKWARD 1869 (to 70)

1448 LOAD_DEREF 0 (self)
1450 LOAD_ATTR 8 (_stop_event)
1452 POP_JUMP_FORWARD_IF_FALSE 25 (to 1464)
1454 LOAD_DEREF 0 (self)
1456 LOAD_ATTR 8 (_stop_event)
1458 LOAD_METHOD 9 (is_set)
1460 CALL 0
1462 POP_JUMP_FORWARD_IF_TRUE 21 (to 1474)

1464 LOAD_DEREF 0 (self)
1466 LOAD_METHOD 6 (_set_progress)
1468 LOAD_CONST 38 ("Selesai.")
1470 CALL 1
1472 POP_TOP

1474 LOAD_DEREF 0 (self)
1476 LOAD_ATTR 11 (root)
1478 LOAD_METHOD 12 (after)
1480 LOAD_CONST 8 (0)
1482 LOAD_CLOSURE 0 (self)
1484 BUILD_TUPLE 1
1486 LOAD_CONST 9 (code object <lambda>)
1488 MAKE_FUNCTION 8 (closure)
1490 CALL 2
1492 POP_TOP

1494 NOP

1496 LOAD_DEREF 0 (self)
1498 LOAD_ATTR 11 (root)
1500 LOAD_METHOD 12 (after)
1502 LOAD_CONST 8 (0)
1504 LOAD_CLOSURE 0 (self)
1506 BUILD_TUPLE 1
1508 LOAD_CONST 10 (code object <lambda>)
1510 MAKE_FUNCTION 8 (closure)
1512 CALL 2
1514 POP_TOP
1516 JUMP_FORWARD 16 (to 1540)
1518 PUSH_EXC_INFO

1520 LOAD_GLOBAL 26 (Exception)
1522 CHECK_EXC_MATCH
1524 POP_JUMP_FORWARD_IF_FALSE 3 (to 1532)
1526 POP_TOP

1528 POP_EXCEPT
1530 JUMP_FORWARD 4 (to 1540)

1532 RERAISE 0
1534 COPY 3
1536 POP_EXCEPT
1538 RERAISE 1

1540 LOAD_DEREF 0 (self)
1542 LOAD_ATTR 8 (_stop_event)
1544 POP_JUMP_FORWARD_IF_FALSE 48 (to 1570)
1546 LOAD_DEREF 0 (self)
1548 LOAD_ATTR 8 (_stop_event)
1550 LOAD_METHOD 9 (is_set)
1552 CALL 0
1554 POP_JUMP_FORWARD_IF_FALSE 25 (to 1574)

1556 LOAD_DEREF 0 (self)
1558 LOAD_METHOD 6 (_set_progress)
1560 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
1562 CALL 1
1564 POP_TOP
1566 LOAD_CONST 0 (None)
1568 RETURN_VALUE

1570 LOAD_CONST 0 (None)
1572 RETURN_VALUE
1574 LOAD_CONST 0 (None)
1576 RETURN_VALUE
1578 PUSH_EXC_INFO

1580 LOAD_DEREF 0 (self)
1582 LOAD_ATTR 11 (root)
1584 LOAD_METHOD 12 (after)
1586 LOAD_CONST 8 (0)
1588 LOAD_CLOSURE 0 (self)
1590 BUILD_TUPLE 1
1592 LOAD_CONST 9 (code object <lambda>)
1594 MAKE_FUNCTION 8 (closure)
1596 CALL 2
1598 POP_TOP

1600 NOP

1602 LOAD_DEREF 0 (self)
1604 LOAD_ATTR 11 (root)
1606 LOAD_METHOD 12 (after)
1608 LOAD_CONST 8 (0)
1610 LOAD_CLOSURE 0 (self)
1612 BUILD_TUPLE 1
1614 LOAD_CONST 10 (code object <lambda>)
1616 MAKE_FUNCTION 8 (closure)
1618 CALL 2
1620 POP_TOP
1622 JUMP_FORWARD 16 (to 1646)
1624 PUSH_EXC_INFO

1626 LOAD_GLOBAL 26 (Exception)
1628 CHECK_EXC_MATCH
1630 POP_JUMP_FORWARD_IF_FALSE 3 (to 1638)
1632 POP_TOP

1634 POP_EXCEPT
1636 JUMP_FORWARD 4 (to 1646)

1638 RERAISE 0
1640 COPY 3
1642 POP_EXCEPT
1644 RERAISE 1

1646 LOAD_DEREF 0 (self)
1648 LOAD_ATTR 8 (_stop_event)
1650 POP_JUMP_FORWARD_IF_FALSE 47 (to 1674)
1652 LOAD_DEREF 0 (self)
1654 LOAD_ATTR 8 (_stop_event)
1656 LOAD_METHOD 9 (is_set)
1658 CALL 0
1660 POP_JUMP_FORWARD_IF_FALSE 23 (to 1676)

1662 LOAD_DEREF 0 (self)
1664 LOAD_METHOD 6 (_set_progress)
1666 LOAD_CONST 11 ("Dihentikan oleh pengguna.")
1668 CALL 1
1670 POP_TOP
1672 RERAISE 0

1674 RERAISE 0
1676 RERAISE 0
1678 COPY 3
1680 POP_EXCEPT
1682 RERAISE 1

0 COPY_FREE_VARS 1

2 LOAD_DEREF 0 (self)
4 LOAD_ATTR 0 (start_btn)
6 LOAD_METHOD 1 (configure)
8 LOAD_GLOBAL 4 (NORMAL)
10 KW_NAMES 1 (('state',))
12 CALL 1
14 RETURN_VALUE

0 COPY_FREE_VARS 1

2 LOAD_DEREF 0 (self)
4 LOAD_ATTR 0 (stop_btn)
6 LOAD_METHOD 1 (configure)
8 LOAD_GLOBAL 4 (DISABLED)
10 KW_NAMES 1 (('state',))
12 CALL 1
14 RETURN_VALUE

0 COPY_FREE_VARS 4

2 BUILD_LIST 0
4 LOAD_FAST 0 (.0)
6 FOR_ITER 47 (to 54)
8 STORE_FAST 1 (i)
10 LOAD_GLOBAL 1 (NULL + str)
12 LOAD_GLOBAL 3 (NULL + Path)
14 LOAD_DEREF 3 (out_dir)
16 CALL 1
18 LOAD_DEREF 2 (base)
20 FORMAT_VALUE 0
22 LOAD_DEREF 4 (suffix)
24 FORMAT_VALUE 0
26 LOAD_CONST 0 ("_")
28 LOAD_FAST 1 (i)
30 LOAD_CONST 1 (1)
32 BINARY_OP 0
34 FORMAT_VALUE 0
36 LOAD_CONST 0 ("_")
38 LOAD_DEREF 5 (ts)
40 FORMAT_VALUE 0
42 LOAD_CONST 2 (".mp4")
44 BUILD_STRING 7
46 BINARY_OP 11
48 CALL 1
50 LIST_APPEND 2
52 JUMP_BACKWARD 48 (to 6)
54 RETURN_VALUE


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_ATTR 0 (_stop_event)
6 POP_JUMP_FORWARD_IF_FALSE 123 (to 82)
8 LOAD_FAST 0 (self)
10 LOAD_ATTR 0 (_stop_event)
12 LOAD_METHOD 1 (is_set)
14 CALL 0
16 POP_JUMP_FORWARD_IF_TRUE 100 (to 86)

18 LOAD_FAST 0 (self)
20 LOAD_ATTR 0 (_stop_event)
22 LOAD_METHOD 2 (set)
24 CALL 0
26 POP_TOP

28 LOAD_FAST 0 (self)
30 LOAD_METHOD 3 (_log)
32 LOAD_CONST 1 ("⏹️ Stop diminta. Menghentikan proses generate...")
34 CALL 1
36 POP_TOP

38 NOP

40 LOAD_FAST 0 (self)
42 LOAD_ATTR 4 (stop_btn)
44 LOAD_METHOD 5 (configure)
46 LOAD_GLOBAL 12 (DISABLED)
48 KW_NAMES 2 (('state',))
50 CALL 1
52 POP_TOP
54 LOAD_CONST 4 (None)
56 RETURN_VALUE
58 PUSH_EXC_INFO

60 LOAD_GLOBAL 14 (Exception)
62 CHECK_EXC_MATCH
64 POP_JUMP_FORWARD_IF_FALSE 4 (to 74)
66 POP_TOP

68 POP_EXCEPT
70 LOAD_CONST 4 (None)
72 RETURN_VALUE

74 RERAISE 0
76 COPY 3
78 POP_EXCEPT
80 RERAISE 1

82 LOAD_CONST 4 (None)
84 RETURN_VALUE
86 LOAD_CONST 4 (None)
88 RETURN_VALUE
90 PUSH_EXC_INFO

92 LOAD_GLOBAL 14 (Exception)
94 CHECK_EXC_MATCH
96 POP_JUMP_FORWARD_IF_FALSE 35 (to 136)
98 STORE_FAST 1 (e)

100 LOAD_FAST 0 (self)
102 LOAD_METHOD 3 (_log)
104 LOAD_CONST 3 ("⚠️ Gagal meminta stop: ")
106 LOAD_FAST 1 (e)
108 FORMAT_VALUE 0
110 BUILD_STRING 2
112 CALL 1
114 POP_TOP
116 POP_EXCEPT
118 LOAD_CONST 4 (None)
120 STORE_FAST 1 (e)
122 DELETE_FAST 1 (e)
124 LOAD_CONST 4 (None)
126 RETURN_VALUE
128 LOAD_CONST 4 (None)
130 STORE_FAST 1 (e)
132 DELETE_FAST 1 (e)
134 RERAISE 1

136 RERAISE 0
138 COPY 3
140 POP_EXCEPT
142 RERAISE 1


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (prompts_text)
4 POP_JUMP_FORWARD_IF_FALSE 37 (to 22)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 0 (prompts_text)
10 LOAD_METHOD 1 (get)
12 LOAD_CONST 1 ("1.0")
14 LOAD_GLOBAL 4 (tk)
16 LOAD_ATTR 3 (END)
18 CALL 2
20 JUMP_FORWARD 1 (to 24)
22 LOAD_CONST 2 ("")
24 LOAD_METHOD 4 (strip)
26 CALL 0
28 STORE_FAST 1 (text)

30 LOAD_FAST 1 (text)
32 POP_JUMP_FORWARD_IF_TRUE 2 (to 38)

34 BUILD_LIST 0
36 RETURN_VALUE

38 LOAD_CONST 3 (code object <listcomp>)
40 MAKE_FUNCTION 0 (No arguments)
42 LOAD_FAST 1 (text)
44 LOAD_METHOD 5 (splitlines)
46 CALL 0
48 GET_ITER
50 CALL 0
52 STORE_FAST 2 (lines)

54 LOAD_CONST 4 (code object <listcomp>)
56 MAKE_FUNCTION 0 (No arguments)
58 LOAD_FAST 2 (lines)
60 GET_ITER
62 CALL 0
64 RETURN_VALUE


0 BUILD_LIST 0
2 LOAD_FAST 0 (.0)
4 FOR_ITER 22 (to 18)
6 STORE_FAST 1 (ln)
8 LOAD_FAST 1 (ln)
10 LOAD_METHOD 0 (strip)
12 CALL 0
14 LIST_APPEND 2
16 JUMP_BACKWARD 23 (to 4)
18 RETURN_VALUE


0 BUILD_LIST 0
2 LOAD_FAST 0 (.0)
4 FOR_ITER 6 (to 18)
6 STORE_FAST 1 (ln)
8 LOAD_FAST 1 (ln)
10 POP_JUMP_BACKWARD_IF_FALSE 4 (to 4)
12 LOAD_FAST 1 (ln)
14 LIST_APPEND 2
16 JUMP_BACKWARD 7 (to 4)
18 RETURN_VALUE


0 LOAD_CONST 1 ('<>:"/\\|?*')
2 STORE_FAST 2 (invalid)

4 LOAD_FAST 2 (invalid)
6 GET_ITER
8 FOR_ITER 24 (to 26)
10 STORE_FAST 3 (ch)

12 LOAD_FAST 1 (s)
14 LOAD_METHOD 0 (replace)
16 LOAD_FAST 3 (ch)
18 LOAD_CONST 2 (" ")
20 CALL 2
22 STORE_FAST 1 (s)
24 JUMP_BACKWARD 25 (to 8)

26 LOAD_CONST 2 (" ")
28 LOAD_METHOD 1 (join)
30 LOAD_FAST 1 (s)
32 LOAD_METHOD 2 (split)
34 CALL 0
36 CALL 1
38 STORE_FAST 1 (s)

40 LOAD_FAST 1 (s)
42 LOAD_METHOD 0 (replace)
44 LOAD_CONST 2 (" ")
46 LOAD_CONST 3 ("_")
48 CALL 2
50 RETURN_VALUE


0 LOAD_DEREF 0 (self)
2 LOAD_ATTR 0 (root)
4 LOAD_METHOD 1 (after)
6 LOAD_CONST 1 (0)
8 LOAD_CLOSURE 1 (msg)
10 LOAD_CLOSURE 0 (self)
12 BUILD_TUPLE 2
14 LOAD_CONST 2 (code object <lambda>)
16 MAKE_FUNCTION 8 (closure)
18 CALL 2
20 POP_TOP
22 LOAD_CONST 0 (None)
24 RETURN_VALUE

0 COPY_FREE_VARS 2

2 LOAD_DEREF 1 (self)
4 LOAD_ATTR 0 (progress_label)
6 LOAD_METHOD 1 (configure)
8 LOAD_DEREF 0 (msg)
10 KW_NAMES 1 (('text',))
12 CALL 1
14 RETURN_VALUE


0 LOAD_DEREF 0 (self)
2 LOAD_ATTR 0 (root)
4 LOAD_METHOD 1 (after)
6 LOAD_CONST 1 (0)
8 LOAD_CLOSURE 1 (msg)
10 LOAD_CLOSURE 0 (self)
12 BUILD_TUPLE 2
14 LOAD_CONST 2 (code object <lambda>)
16 MAKE_FUNCTION 8 (closure)
18 CALL 2
20 POP_TOP
22 LOAD_CONST 0 (None)
24 RETURN_VALUE

0 COPY_FREE_VARS 2

2 LOAD_DEREF 1 (self)
4 LOAD_METHOD 0 (log)
6 LOAD_DEREF 0 (msg)
8 CALL 1
10 RETURN_VALUE


0 NOP

2 LOAD_GLOBAL 1 (NULL + len)
4 LOAD_FAST 0 (self)
6 LOAD_METHOD 1 (_collect_prompts)
8 CALL 0
10 CALL 1
12 STORE_FAST 1 (cnt)

14 LOAD_FAST 0 (self)
16 LOAD_ATTR 2 (prompt_count_var)
18 LOAD_METHOD 3 (set)
20 LOAD_CONST 1 ("Jumlah prompt: ")
22 LOAD_FAST 1 (cnt)
24 FORMAT_VALUE 0
26 BUILD_STRING 2
28 CALL 1
30 POP_TOP
32 LOAD_CONST 0 (None)
34 RETURN_VALUE
36 PUSH_EXC_INFO

38 LOAD_GLOBAL 8 (Exception)
40 CHECK_EXC_MATCH
42 POP_JUMP_FORWARD_IF_FALSE 35 (to 82)
44 STORE_FAST 2 (e)

46 LOAD_FAST 0 (self)
48 LOAD_METHOD 5 (_log)
50 LOAD_CONST 2 ("⚠️ Gagal update jumlah prompt: ")
52 LOAD_FAST 2 (e)
54 FORMAT_VALUE 0
56 BUILD_STRING 2
58 CALL 1
60 POP_TOP
62 POP_EXCEPT
64 LOAD_CONST 0 (None)
66 STORE_FAST 2 (e)
68 DELETE_FAST 2 (e)
70 LOAD_CONST 0 (None)
72 RETURN_VALUE
74 LOAD_CONST 0 (None)
76 STORE_FAST 2 (e)
78 DELETE_FAST 2 (e)
80 RERAISE 1

82 RERAISE 0
84 COPY 3
86 POP_EXCEPT
88 RERAISE 1


0 LOAD_FAST 1 (err_msg)
2 JUMP_IF_TRUE_OR_POP 1 (to 6)
4 LOAD_CONST 1 ("")
6 LOAD_METHOD 0 (lower)
8 CALL 0
10 STORE_DEREF 3 (msg)

12 BUILD_LIST 0
14 LOAD_CONST 2 (('quota', 'exhaust', 'permission', 'forbidden', '403', '429', 'unauthorized', 'invalid api key', 'api key not valid', 'not have permission'))
16 LIST_EXTEND 1
18 STORE_FAST 2 (keywords)

20 LOAD_GLOBAL 3 (NULL + any)
22 LOAD_CLOSURE 3 (msg)
24 BUILD_TUPLE 1
26 LOAD_CONST 3 (code object <genexpr>)
28 MAKE_FUNCTION 8 (closure)
30 LOAD_FAST 2 (keywords)
32 GET_ITER
34 CALL 0
36 CALL 1
38 RETURN_VALUE

0 COPY_FREE_VARS 1

2 RETURN_GENERATOR
4 POP_TOP
6 LOAD_FAST 0 (.0)
8 FOR_ITER 8 (to 24)
10 STORE_FAST 1 (k)
12 LOAD_FAST 1 (k)
14 LOAD_DEREF 2 (msg)
16 CONTAINS_OP 0 (in)
18 YIELD_VALUE
20 POP_TOP
22 JUMP_BACKWARD 9 (to 8)
24 LOAD_CONST 0 (None)
26 RETURN_VALUE