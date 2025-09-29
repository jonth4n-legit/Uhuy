Sorry: IndentationError: unexpected indent (indented_0.py, line 140)

<module>: Success: Equal

<module>._get_bundle_root: Success: Equal

***<module>._ensure_playwright_browsers_path: Failure detected at line number 44 and instruction offset 26: Different bytecode

<module>.CloudSkillAutomation: Success: Equal

<module>.CloudSkillAutomation.__init__: Success: Equal

<module>.CloudSkillAutomation.get_default_pw_state_path: Success: Equal

<module>.CloudSkillAutomation.get_default_pw_profile_dir: Success: Equal

<module>.CloudSkillAutomation._ensure_loop: Success: Equal

***<module>.CloudSkillAutomation._ensure_loop._runner: Failure: Different bytecode

<module>.CloudSkillAutomation._run_async: Success: Equal

<module>.CloudSkillAutomation.register_account: Success: Equal

***<module>.CloudSkillAutomation._register_account_async: Failure: Compilation Error

***<module>.CloudSkillAutomation._is_confirmation_success: Failure: Compilation Error

***<module>.CloudSkillAutomation._bind_single_page_policy: Failure: Compilation Error

***<module>.CloudSkillAutomation._bind_single_page_policy._handler: Failure: Compilation Error

***<module>.CloudSkillAutomation._bind_single_page_policy.<lambda>, None: Failure: Missing bytecode

<module>.CloudSkillAutomation._unbind_page_policy: Success: Equal

<module>.CloudSkillAutomation.confirm_via_link: Success: Equal

<module>.CloudSkillAutomation.start_lab: Success: Equal

***<module>.CloudSkillAutomation._start_lab_async: Failure: Compilation Error

***<module>.CloudSkillAutomation._start_lab_async.<lambda>, None: Failure: Missing bytecode

<module>.CloudSkillAutomation.shutdown: Success: Equal

***<module>.CloudSkillAutomation._confirm_via_link_async: Failure: Compilation Error

***<module>.CloudSkillAutomation._ensure_page_ready: Failure: Compilation Error

***<module>.CloudSkillAutomation._close_other_pages: Failure: Compilation Error

***<module>.CloudSkillAutomation._init_browser: Failure: Compilation Error

***<module>.CloudSkillAutomation._navigate_to_registration: Failure: Compilation Error

***<module>.CloudSkillAutomation._fill_registration_form: Failure: Compilation Error

***<module>.CloudSkillAutomation._fill_registration_form.smart_fill_field: Failure: Compilation Error

***<module>.CloudSkillAutomation._fill_registration_form.deep_fill_field: Failure: Compilation Error

***<module>.CloudSkillAutomation._fill_registration_form.<listcomp>, None: Failure: Missing bytecode

***<module>.CloudSkillAutomation._fill_registration_form.<listcomp>, None: Failure: Missing bytecode

***<module>.CloudSkillAutomation._fill_registration_form.<listcomp>, None: Failure: Missing bytecode

***<module>.CloudSkillAutomation._fill_birth_date: Failure: Compilation Error

***<module>.CloudSkillAutomation._handle_newsletter_checkbox: Failure: Different control flow

<module>.CloudSkillAutomation._find_recaptcha_frames: Success: Equal

***<module>.CloudSkillAutomation._scroll_to_recaptcha: Failure: Compilation Error

***<module>.CloudSkillAutomation._click_recaptcha_checkbox: Failure: Compilation Error

***<module>.CloudSkillAutomation._handle_captcha: Failure: Compilation Error

***<module>.CloudSkillAutomation._wait_for_manual_captcha_solve: Failure: Compilation Error

***<module>.CloudSkillAutomation._solve_audio_captcha: Failure: Compilation Error

***<module>.CloudSkillAutomation._solve_audio_captcha.is_audio_resp: Failure: Different bytecode

***<module>.CloudSkillAutomation._is_captcha_solved: Failure: Different control flow

<module>.CloudSkillAutomation._submit_form: Success: Equal

***<module>.CloudSkillAutomation._wait_for_result: Failure: Compilation Error

***<module>.CloudSkillAutomation._cleanup: Failure: Compilation Error









0 LOAD_CONST 0 ("\nAutomation untuk registrasi akun Google Cloud Skills Boost\n")
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (None)
8 IMPORT_NAME 1 (asyncio)
10 STORE_NAME 1 (asyncio)

12 LOAD_CONST 1 (0)
14 LOAD_CONST 3 (('async_playwright', 'Page', 'Browser', 'BrowserContext'))
16 IMPORT_NAME 2 (playwright.async_api)
18 IMPORT_FROM 3 (async_playwright)
20 STORE_NAME 3 (async_playwright)
22 IMPORT_FROM 4 (Page)
24 STORE_NAME 4 (Page)
26 IMPORT_FROM 5 (Browser)
28 STORE_NAME 5 (Browser)
30 IMPORT_FROM 6 (BrowserContext)
32 STORE_NAME 6 (BrowserContext)
34 POP_TOP

36 LOAD_CONST 1 (0)
38 LOAD_CONST 4 (('urlparse', 'parse_qs'))
40 IMPORT_NAME 7 (urllib.parse)
42 IMPORT_FROM 8 (urlparse)
44 STORE_NAME 8 (urlparse)
46 IMPORT_FROM 9 (parse_qs)
48 STORE_NAME 9 (parse_qs)
50 POP_TOP

52 LOAD_CONST 1 (0)
54 LOAD_CONST 2 (None)
56 IMPORT_NAME 10 (time)
58 STORE_NAME 10 (time)

60 LOAD_CONST 1 (0)
62 LOAD_CONST 2 (None)
64 IMPORT_NAME 11 (base64)
66 STORE_NAME 11 (base64)

68 LOAD_CONST 1 (0)
70 LOAD_CONST 5 (('Dict', 'Optional'))
72 IMPORT_NAME 12 (typing)
74 IMPORT_FROM 13 (Dict)
76 STORE_NAME 13 (Dict)
78 IMPORT_FROM 14 (Optional)
80 STORE_NAME 14 (Optional)
82 POP_TOP

84 LOAD_CONST 1 (0)
86 LOAD_CONST 6 (('Path',))
88 IMPORT_NAME 15 (pathlib)
90 IMPORT_FROM 16 (Path)
92 STORE_NAME 16 (Path)
94 POP_TOP

96 LOAD_CONST 1 (0)
98 LOAD_CONST 2 (None)
100 IMPORT_NAME 17 (logging)
102 STORE_NAME 17 (logging)

104 LOAD_CONST 1 (0)
106 LOAD_CONST 2 (None)
108 IMPORT_NAME 18 (os)
110 STORE_NAME 18 (os)

112 LOAD_CONST 1 (0)
114 LOAD_CONST 2 (None)
116 IMPORT_NAME 19 (sys)
118 STORE_NAME 19 (sys)

120 LOAD_CONST 1 (0)
122 LOAD_CONST 2 (None)
124 IMPORT_NAME 20 (threading)
126 STORE_NAME 20 (threading)

128 LOAD_CONST 1 (0)
130 LOAD_CONST 2 (None)
132 IMPORT_NAME 21 (concurrent.futures)
134 STORE_NAME 22 (concurrent)

136 LOAD_CONST 1 (0)
138 LOAD_CONST 7 (('start_lab', 'open_cloud_console', 'handle_gcloud_terms', 'enable_genai_and_create_api_key'))
140 IMPORT_NAME 23 (automation.lab_actions_simple)
142 IMPORT_FROM 24 (start_lab)
144 STORE_NAME 25 (start_lab_action)
146 IMPORT_FROM 26 (open_cloud_console)
148 STORE_NAME 27 (open_console_action)
150 IMPORT_FROM 28 (handle_gcloud_terms)
152 STORE_NAME 29 (handle_terms_action)
154 IMPORT_FROM 30 (enable_genai_and_create_api_key)
156 STORE_NAME 31 (enable_key_action)
158 POP_TOP

160 LOAD_CONST 1 (0)
162 LOAD_CONST 8 (('confirm_via_link_action',))
164 IMPORT_NAME 32 (automation.confirm_actions)
166 IMPORT_FROM 33 (confirm_via_link_action)
168 STORE_NAME 33 (confirm_via_link_action)
170 POP_TOP

172 LOAD_CONST 1 (0)
174 LOAD_CONST 9 (('setup_logger', 'log_automation_step'))
176 IMPORT_NAME 34 (utils.logger)
178 IMPORT_FROM 35 (setup_logger)
180 STORE_NAME 35 (setup_logger)
182 IMPORT_FROM 36 (log_automation_step)
184 STORE_NAME 36 (log_automation_step)
186 POP_TOP

188 LOAD_CONST 1 (0)
190 LOAD_CONST 10 (('settings',))
192 IMPORT_NAME 37 (config.settings)
194 IMPORT_FROM 38 (settings)
196 STORE_NAME 38 (settings)
198 POP_TOP

200 LOAD_CONST 11 ("return")
202 LOAD_NAME 16 (Path)
204 BUILD_TUPLE 2
206 LOAD_CONST 12 (code object _get_bundle_root)
208 MAKE_FUNCTION 4 (annotation)
210 STORE_NAME 39 (_get_bundle_root)

212 LOAD_CONST 26 (('return', None))
214 LOAD_CONST 13 (code object _ensure_playwright_browsers_path)
216 MAKE_FUNCTION 4 (annotation)
218 STORE_NAME 40 (_ensure_playwright_browsers_path)

220 PUSH_NULL
222 LOAD_BUILD_CLASS
224 LOAD_CONST 14 (code object CloudSkillAutomation)
226 MAKE_FUNCTION 0 (No arguments)
228 LOAD_CONST 15 ("CloudSkillAutomation")
230 CALL 2
232 STORE_NAME 41 (CloudSkillAutomation)

234 LOAD_NAME 42 (__name__)
236 LOAD_CONST 16 ("__main__")
238 COMPARE_OP 2 (==)
240 POP_JUMP_FORWARD_IF_FALSE 57 (to 300)

242 LOAD_CONST 17 ("John")

244 LOAD_CONST 18 ("Doe")

246 LOAD_CONST 19 ("john.doe@example.com")

248 LOAD_CONST 20 ("TechCorp")

250 LOAD_CONST 21 ("SecurePass123!")
252 LOAD_CONST 22 (('first_name', 'last_name', 'email', 'company', 'password'))
254 BUILD_CONST_KEY_MAP 5
256 STORE_NAME 43 (test_data)

258 PUSH_NULL
260 LOAD_NAME 41 (CloudSkillAutomation)
262 LOAD_CONST 23 (False)
264 KW_NAMES 24 (('headless',))
266 CALL 1
268 STORE_NAME 44 (automation)

270 LOAD_NAME 44 (automation)
272 LOAD_METHOD 45 (register_account)
274 LOAD_NAME 43 (test_data)
276 CALL 1
278 STORE_NAME 46 (result)

280 PUSH_NULL
282 LOAD_NAME 47 (print)
284 LOAD_CONST 25 ("Registration result: ")
286 LOAD_NAME 46 (result)
288 FORMAT_VALUE 0
290 BUILD_STRING 2
292 CALL 1
294 POP_TOP
296 LOAD_CONST 2 (None)
298 RETURN_VALUE

300 LOAD_CONST 2 (None)
302 RETURN_VALUE


0 LOAD_GLOBAL 1 (NULL + getattr)
2 LOAD_GLOBAL 2 (sys)
4 LOAD_CONST 1 ("_MEIPASS")
6 LOAD_CONST 2 (None)
8 CALL 3
10 STORE_FAST 0 (base_meipass)

12 LOAD_FAST 0 (base_meipass)
14 POP_JUMP_FORWARD_IF_FALSE 15 (to 24)

16 LOAD_GLOBAL 5 (NULL + Path)
18 LOAD_FAST 0 (base_meipass)
20 CALL 1
22 RETURN_VALUE

24 LOAD_GLOBAL 1 (NULL + getattr)
26 LOAD_GLOBAL 2 (sys)
28 LOAD_CONST 3 ("frozen")
30 LOAD_CONST 4 (False)
32 CALL 3
34 POP_JUMP_FORWARD_IF_FALSE 48 (to 52)

36 LOAD_GLOBAL 5 (NULL + Path)
38 LOAD_GLOBAL 2 (sys)
40 LOAD_ATTR 3 (executable)
42 CALL 1
44 LOAD_METHOD 4 (resolve)
46 CALL 0
48 LOAD_ATTR 5 (parent)
50 RETURN_VALUE

52 LOAD_GLOBAL 5 (NULL + Path)
54 LOAD_GLOBAL 12 (__file__)
56 CALL 1
58 LOAD_METHOD 4 (resolve)
60 CALL 0
62 LOAD_ATTR 5 (parent)
64 LOAD_ATTR 5 (parent)
66 RETURN_VALUE


0 LOAD_GLOBAL 0 (os)
2 LOAD_ATTR 1 (environ)
4 LOAD_METHOD 2 (get)
6 LOAD_CONST 1 ("PLAYWRIGHT_BROWSERS_PATH")
8 CALL 1
10 POP_JUMP_FORWARD_IF_FALSE 2 (to 16)

12 LOAD_CONST 2 (None)
14 RETURN_VALUE

16 NOP

18 LOAD_GLOBAL 7 (NULL + _get_bundle_root)
20 CALL 0
22 STORE_FAST 0 (base)

24 LOAD_FAST 0 (base)
26 LOAD_CONST 3 ("ms-playwright")
28 BINARY_OP 11
30 STORE_FAST 1 (ms_dir)

32 LOAD_FAST 1 (ms_dir)
34 LOAD_METHOD 4 (exists)
36 CALL 0
38 POP_JUMP_FORWARD_IF_FALSE 30 (to 58)

40 LOAD_GLOBAL 11 (NULL + str)
42 LOAD_FAST 1 (ms_dir)
44 CALL 1
46 LOAD_GLOBAL 0 (os)
48 LOAD_ATTR 1 (environ)
50 LOAD_CONST 1 ("PLAYWRIGHT_BROWSERS_PATH")
52 STORE_SUBSCR
54 LOAD_CONST 2 (None)
56 RETURN_VALUE

58 LOAD_CONST 2 (None)
60 RETURN_VALUE
62 PUSH_EXC_INFO

64 LOAD_GLOBAL 12 (Exception)
66 CHECK_EXC_MATCH
68 POP_JUMP_FORWARD_IF_FALSE 4 (to 78)
70 POP_TOP

72 POP_EXCEPT
74 LOAD_CONST 2 (None)
76 RETURN_VALUE

78 RERAISE 0
80 COPY 3
82 POP_EXCEPT
84 RERAISE 1


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("CloudSkillAutomation")
6 STORE_NAME 2 (__qualname__)

8 LOAD_CONST 1 ("Automation untuk registrasi Google Cloud Skills Boost")
10 STORE_NAME 3 (__doc__)

12 LOAD_CONST 53 ((False, None, False, False))
14 LOAD_CONST 4 ("headless")
16 LOAD_NAME 4 (bool)
18 LOAD_CONST 5 ("keep_browser_open")
20 LOAD_NAME 4 (bool)
22 LOAD_CONST 6 ("extension_mode")
24 LOAD_NAME 4 (bool)
26 BUILD_TUPLE 6
28 LOAD_CONST 7 (code object __init__)
30 MAKE_FUNCTION 5 (default, annotation)
32 STORE_NAME 5 (__init__)

34 LOAD_NAME 6 (staticmethod)

36 LOAD_CONST 8 ("return")
38 LOAD_NAME 7 (str)
40 BUILD_TUPLE 2
42 LOAD_CONST 9 (code object get_default_pw_state_path)
44 MAKE_FUNCTION 4 (annotation)

46 CALL 0

48 STORE_NAME 8 (get_default_pw_state_path)

50 LOAD_NAME 6 (staticmethod)

52 LOAD_CONST 8 ("return")
54 LOAD_NAME 7 (str)
56 BUILD_TUPLE 2
58 LOAD_CONST 10 (code object get_default_pw_profile_dir)
60 MAKE_FUNCTION 4 (annotation)

62 CALL 0

64 STORE_NAME 9 (get_default_pw_profile_dir)

66 LOAD_CONST 54 (('return', None))
68 LOAD_CONST 11 (code object _ensure_loop)
70 MAKE_FUNCTION 4 (annotation)
72 STORE_NAME 10 (_ensure_loop)

74 LOAD_CONST 12 (code object _run_async)
76 MAKE_FUNCTION 0 (No arguments)
78 STORE_NAME 11 (_run_async)

80 LOAD_CONST 13 ("user_data")
82 LOAD_NAME 12 (Dict)
84 LOAD_CONST 8 ("return")
86 LOAD_NAME 12 (Dict)
88 BUILD_TUPLE 4
90 LOAD_CONST 14 (code object register_account)
92 MAKE_FUNCTION 4 (annotation)
94 STORE_NAME 13 (register_account)

96 LOAD_CONST 13 ("user_data")
98 LOAD_NAME 12 (Dict)
100 LOAD_CONST 8 ("return")
102 LOAD_NAME 12 (Dict)
104 BUILD_TUPLE 4
106 LOAD_CONST 15 (code object _register_account_async)
108 MAKE_FUNCTION 4 (annotation)
110 STORE_NAME 14 (_register_account_async)

112 LOAD_CONST 8 ("return")
114 LOAD_NAME 4 (bool)
116 BUILD_TUPLE 2
118 LOAD_CONST 16 (code object _is_confirmation_success)
120 MAKE_FUNCTION 4 (annotation)
122 STORE_NAME 15 (_is_confirmation_success)

124 LOAD_CONST 17 (code object _bind_single_page_policy)
126 MAKE_FUNCTION 0 (No arguments)
128 STORE_NAME 16 (_bind_single_page_policy)

130 LOAD_CONST 18 (code object _unbind_page_policy)
132 MAKE_FUNCTION 0 (No arguments)
134 STORE_NAME 17 (_unbind_page_policy)

136 LOAD_CONST 55 ((None,))
138 LOAD_CONST 19 ("url")
140 LOAD_NAME 7 (str)
142 LOAD_CONST 20 ("password")
144 LOAD_NAME 7 (str)
146 LOAD_CONST 21 ("email")
148 LOAD_NAME 18 (Optional)
150 LOAD_NAME 7 (str)
152 BINARY_SUBSCR
154 LOAD_CONST 8 ("return")
156 LOAD_NAME 12 (Dict)
158 BUILD_TUPLE 8
160 LOAD_CONST 22 (code object confirm_via_link)
162 MAKE_FUNCTION 5 (default, annotation)
164 STORE_NAME 19 (confirm_via_link)

166 LOAD_CONST 23 ("lab_url")
168 LOAD_NAME 7 (str)
170 LOAD_CONST 8 ("return")
172 LOAD_NAME 12 (Dict)
174 BUILD_TUPLE 4
176 LOAD_CONST 24 (code object start_lab)
178 MAKE_FUNCTION 4 (annotation)
180 STORE_NAME 20 (start_lab)

182 LOAD_CONST 23 ("lab_url")
184 LOAD_NAME 7 (str)
186 LOAD_CONST 8 ("return")
188 LOAD_NAME 12 (Dict)
190 BUILD_TUPLE 4
192 LOAD_CONST 25 (code object _start_lab_async)
194 MAKE_FUNCTION 4 (annotation)
196 STORE_NAME 21 (_start_lab_async)

198 LOAD_CONST 54 (('return', None))
200 LOAD_CONST 26 (code object shutdown)
202 MAKE_FUNCTION 4 (annotation)
204 STORE_NAME 22 (shutdown)

206 LOAD_CONST 55 ((None,))
208 LOAD_CONST 19 ("url")
210 LOAD_NAME 7 (str)
212 LOAD_CONST 20 ("password")
214 LOAD_NAME 7 (str)
216 LOAD_CONST 21 ("email")
218 LOAD_NAME 18 (Optional)
220 LOAD_NAME 7 (str)
222 BINARY_SUBSCR
224 LOAD_CONST 8 ("return")
226 LOAD_NAME 12 (Dict)
228 BUILD_TUPLE 8
230 LOAD_CONST 27 (code object _confirm_via_link_async)
232 MAKE_FUNCTION 5 (default, annotation)
234 STORE_NAME 23 (_confirm_via_link_async)

236 LOAD_CONST 28 (code object _ensure_page_ready)
238 MAKE_FUNCTION 0 (No arguments)
240 STORE_NAME 24 (_ensure_page_ready)

242 LOAD_CONST 56 ((True,))
244 LOAD_CONST 30 ("keep_current")
246 LOAD_NAME 4 (bool)
248 LOAD_CONST 8 ("return")
250 LOAD_CONST 3 (None)
252 BUILD_TUPLE 4
254 LOAD_CONST 31 (code object _close_other_pages)
256 MAKE_FUNCTION 5 (default, annotation)
258 STORE_NAME 25 (_close_other_pages)

260 LOAD_CONST 32 (code object _init_browser)
262 MAKE_FUNCTION 0 (No arguments)
264 STORE_NAME 26 (_init_browser)

266 LOAD_CONST 33 (code object _navigate_to_registration)
268 MAKE_FUNCTION 0 (No arguments)
270 STORE_NAME 27 (_navigate_to_registration)

272 LOAD_CONST 13 ("user_data")
274 LOAD_NAME 12 (Dict)
276 BUILD_TUPLE 2
278 LOAD_CONST 34 (code object _fill_registration_form)
280 MAKE_FUNCTION 4 (annotation)
282 STORE_NAME 28 (_fill_registration_form)

284 LOAD_CONST 35 (code object _fill_birth_date)
286 MAKE_FUNCTION 0 (No arguments)
288 STORE_NAME 29 (_fill_birth_date)

290 LOAD_CONST 36 (code object _handle_newsletter_checkbox)
292 MAKE_FUNCTION 0 (No arguments)
294 STORE_NAME 30 (_handle_newsletter_checkbox)

296 LOAD_CONST 37 (code object _find_recaptcha_frames)
298 MAKE_FUNCTION 0 (No arguments)
300 STORE_NAME 31 (_find_recaptcha_frames)

302 LOAD_CONST 57 ((8, False, False))
304 LOAD_CONST 39 ("max_steps")
306 LOAD_NAME 32 (int)
308 LOAD_CONST 40 ("fast")
310 LOAD_NAME 4 (bool)
312 LOAD_CONST 41 ("skip_fallback")
314 LOAD_NAME 4 (bool)
316 LOAD_CONST 8 ("return")
318 LOAD_NAME 4 (bool)
320 BUILD_TUPLE 8
322 LOAD_CONST 42 (code object _scroll_to_recaptcha)
324 MAKE_FUNCTION 5 (default, annotation)
326 STORE_NAME 33 (_scroll_to_recaptcha)

328 LOAD_CONST 8 ("return")
330 LOAD_NAME 4 (bool)
332 BUILD_TUPLE 2
334 LOAD_CONST 43 (code object _click_recaptcha_checkbox)
336 MAKE_FUNCTION 4 (annotation)
338 STORE_NAME 34 (_click_recaptcha_checkbox)

340 LOAD_CONST 8 ("return")
342 LOAD_NAME 4 (bool)
344 BUILD_TUPLE 2
346 LOAD_CONST 44 (code object _handle_captcha)
348 MAKE_FUNCTION 4 (annotation)
350 STORE_NAME 35 (_handle_captcha)

352 LOAD_CONST 58 ((180,))
354 LOAD_CONST 46 ("timeout")
356 LOAD_NAME 32 (int)
358 LOAD_CONST 8 ("return")
360 LOAD_NAME 4 (bool)
362 BUILD_TUPLE 4
364 LOAD_CONST 47 (code object _wait_for_manual_captcha_solve)
366 MAKE_FUNCTION 5 (default, annotation)
368 STORE_NAME 36 (_wait_for_manual_captcha_solve)

370 LOAD_CONST 8 ("return")
372 LOAD_NAME 4 (bool)
374 BUILD_TUPLE 2
376 LOAD_CONST 48 (code object _solve_audio_captcha)
378 MAKE_FUNCTION 4 (annotation)
380 STORE_NAME 37 (_solve_audio_captcha)

382 LOAD_CONST 8 ("return")
384 LOAD_NAME 4 (bool)
386 BUILD_TUPLE 2
388 LOAD_CONST 49 (code object _is_captcha_solved)
390 MAKE_FUNCTION 4 (annotation)
392 STORE_NAME 38 (_is_captcha_solved)

394 LOAD_CONST 50 (code object _submit_form)
396 MAKE_FUNCTION 0 (No arguments)
398 STORE_NAME 39 (_submit_form)

400 LOAD_CONST 8 ("return")
402 LOAD_NAME 12 (Dict)
404 BUILD_TUPLE 2
406 LOAD_CONST 51 (code object _wait_for_result)
408 MAKE_FUNCTION 4 (annotation)
410 STORE_NAME 40 (_wait_for_result)

412 LOAD_CONST 52 (code object _cleanup)
414 MAKE_FUNCTION 0 (No arguments)
416 STORE_NAME 41 (_cleanup)
418 LOAD_CONST 3 (None)
420 RETURN_VALUE


0 LOAD_FAST 1 (headless)
2 LOAD_FAST 0 (self)
4 STORE_ATTR 0 (headless)

6 LOAD_FAST 2 (captcha_solver)
8 LOAD_FAST 0 (self)
10 STORE_ATTR 1 (captcha_solver)

12 LOAD_GLOBAL 5 (NULL + setup_logger)
14 LOAD_CONST 1 ("CloudSkillAutomation")
16 CALL 1
18 LOAD_FAST 0 (self)
20 STORE_ATTR 3 (logger)

22 LOAD_CONST 2 (None)
24 LOAD_FAST 0 (self)
26 STORE_ATTR 4 (browser)

28 LOAD_CONST 2 (None)
30 LOAD_FAST 0 (self)
32 STORE_ATTR 5 (context)

34 LOAD_CONST 2 (None)
36 LOAD_FAST 0 (self)
38 STORE_ATTR 6 (page)

40 LOAD_GLOBAL 15 (NULL + bool)
42 LOAD_FAST 4 (extension_mode)
44 CALL 1
46 LOAD_FAST 0 (self)
48 STORE_ATTR 8 (extension_mode)

50 LOAD_FAST 3 (keep_browser_open)
52 LOAD_FAST 0 (self)
54 STORE_ATTR 9 (keep_browser_open)

56 LOAD_CONST 3 ("redirect")
58 LOAD_FAST 0 (self)
60 STORE_ATTR 10 (_popup_mode)

62 LOAD_CONST 2 (None)
64 LOAD_FAST 0 (self)
66 STORE_ATTR 11 (_loop)

68 LOAD_CONST 2 (None)
70 LOAD_FAST 0 (self)
72 STORE_ATTR 12 (_loop_thread)

74 LOAD_CONST 2 (None)
76 LOAD_FAST 0 (self)
78 STORE_ATTR 13 (_loop_ready_evt)
80 LOAD_CONST 2 (None)
82 RETURN_VALUE


0 LOAD_CONST 1 (None)
2 STORE_FAST 0 (base)

4 NOP

6 LOAD_GLOBAL 0 (os)
8 LOAD_ATTR 1 (environ)
10 LOAD_METHOD 2 (get)
12 LOAD_CONST 2 ("LOCALAPPDATA")
14 CALL 1
16 STORE_FAST 0 (base)
18 JUMP_FORWARD 18 (to 46)
20 PUSH_EXC_INFO

22 LOAD_GLOBAL 6 (Exception)
24 CHECK_EXC_MATCH
26 POP_JUMP_FORWARD_IF_FALSE 5 (to 38)
28 POP_TOP

30 LOAD_CONST 1 (None)
32 STORE_FAST 0 (base)
34 POP_EXCEPT
36 JUMP_FORWARD 4 (to 46)

38 RERAISE 0
40 COPY 3
42 POP_EXCEPT
44 RERAISE 1

46 LOAD_FAST 0 (base)
48 POP_JUMP_FORWARD_IF_TRUE 99 (to 108)

50 NOP

52 LOAD_GLOBAL 0 (os)
54 LOAD_ATTR 4 (path)
56 LOAD_METHOD 5 (join)
58 LOAD_GLOBAL 0 (os)
60 LOAD_ATTR 4 (path)
62 LOAD_METHOD 6 (expanduser)
64 LOAD_CONST 3 ("~")
66 CALL 1
68 LOAD_CONST 4 ("AppData")
70 LOAD_CONST 5 ("Local")
72 CALL 3
74 STORE_FAST 0 (base)
76 JUMP_FORWARD 35 (to 108)
78 PUSH_EXC_INFO

80 LOAD_GLOBAL 6 (Exception)
82 CHECK_EXC_MATCH
84 POP_JUMP_FORWARD_IF_FALSE 22 (to 100)
86 POP_TOP

88 LOAD_GLOBAL 1 (NULL + os)
90 LOAD_ATTR 7 (getcwd)
92 CALL 0
94 STORE_FAST 0 (base)
96 POP_EXCEPT
98 JUMP_FORWARD 4 (to 108)

100 RERAISE 0
102 COPY 3
104 POP_EXCEPT
106 RERAISE 1

108 LOAD_GLOBAL 0 (os)
110 LOAD_ATTR 4 (path)
112 LOAD_METHOD 5 (join)
114 LOAD_FAST 0 (base)
116 LOAD_CONST 6 ("AutoCloudSkill")
118 LOAD_CONST 7 ("playwright")
120 CALL 3
122 STORE_FAST 1 (state_dir)

124 LOAD_GLOBAL 0 (os)
126 LOAD_ATTR 4 (path)
128 LOAD_METHOD 5 (join)
130 LOAD_FAST 1 (state_dir)
132 LOAD_CONST 8 (".pw-state.json")
134 CALL 2
136 RETURN_VALUE


0 LOAD_CONST 1 (None)
2 STORE_FAST 0 (base)

4 NOP

6 LOAD_GLOBAL 0 (os)
8 LOAD_ATTR 1 (environ)
10 LOAD_METHOD 2 (get)
12 LOAD_CONST 2 ("LOCALAPPDATA")
14 CALL 1
16 STORE_FAST 0 (base)
18 JUMP_FORWARD 18 (to 46)
20 PUSH_EXC_INFO

22 LOAD_GLOBAL 6 (Exception)
24 CHECK_EXC_MATCH
26 POP_JUMP_FORWARD_IF_FALSE 5 (to 38)
28 POP_TOP

30 LOAD_CONST 1 (None)
32 STORE_FAST 0 (base)
34 POP_EXCEPT
36 JUMP_FORWARD 4 (to 46)

38 RERAISE 0
40 COPY 3
42 POP_EXCEPT
44 RERAISE 1

46 LOAD_FAST 0 (base)
48 POP_JUMP_FORWARD_IF_TRUE 99 (to 108)

50 NOP

52 LOAD_GLOBAL 0 (os)
54 LOAD_ATTR 4 (path)
56 LOAD_METHOD 5 (join)
58 LOAD_GLOBAL 0 (os)
60 LOAD_ATTR 4 (path)
62 LOAD_METHOD 6 (expanduser)
64 LOAD_CONST 3 ("~")
66 CALL 1
68 LOAD_CONST 4 ("AppData")
70 LOAD_CONST 5 ("Local")
72 CALL 3
74 STORE_FAST 0 (base)
76 JUMP_FORWARD 35 (to 108)
78 PUSH_EXC_INFO

80 LOAD_GLOBAL 6 (Exception)
82 CHECK_EXC_MATCH
84 POP_JUMP_FORWARD_IF_FALSE 22 (to 100)
86 POP_TOP

88 LOAD_GLOBAL 1 (NULL + os)
90 LOAD_ATTR 7 (getcwd)
92 CALL 0
94 STORE_FAST 0 (base)
96 POP_EXCEPT
98 JUMP_FORWARD 4 (to 108)

100 RERAISE 0
102 COPY 3
104 POP_EXCEPT
106 RERAISE 1

108 LOAD_GLOBAL 0 (os)
110 LOAD_ATTR 4 (path)
112 LOAD_METHOD 5 (join)
114 LOAD_FAST 0 (base)
116 LOAD_CONST 6 ("AutoCloudSkill")
118 LOAD_CONST 7 ("playwright")
120 LOAD_CONST 8 ("profile")
122 CALL 4
124 RETURN_VALUE


0 LOAD_DEREF 0 (self)
2 LOAD_ATTR 0 (_loop)
4 POP_JUMP_FORWARD_IF_FALSE 34 (to 26)
6 LOAD_DEREF 0 (self)
8 LOAD_ATTR 1 (_loop_thread)
10 POP_JUMP_FORWARD_IF_FALSE 27 (to 26)
12 LOAD_DEREF 0 (self)
14 LOAD_ATTR 1 (_loop_thread)
16 LOAD_METHOD 2 (is_alive)
18 CALL 0
20 POP_JUMP_FORWARD_IF_FALSE 2 (to 26)

22 LOAD_CONST 0 (None)
24 RETURN_VALUE

26 LOAD_GLOBAL 7 (NULL + threading)
28 LOAD_ATTR 4 (Event)
30 CALL 0
32 LOAD_DEREF 0 (self)
34 STORE_ATTR 5 (_loop_ready_evt)

36 LOAD_CLOSURE 0 (self)
38 BUILD_TUPLE 1
40 LOAD_CONST 1 (code object _runner)
42 MAKE_FUNCTION 8 (closure)
44 STORE_FAST 1 (_runner)

46 LOAD_GLOBAL 7 (NULL + threading)
48 LOAD_ATTR 6 (Thread)
50 LOAD_FAST 1 (_runner)
52 LOAD_CONST 2 (True)
54 KW_NAMES 3 (('target', 'daemon'))
56 CALL 2
58 LOAD_DEREF 0 (self)
60 STORE_ATTR 1 (_loop_thread)

62 LOAD_DEREF 0 (self)
64 LOAD_ATTR 1 (_loop_thread)
66 LOAD_METHOD 7 (start)
68 CALL 0
70 POP_TOP

72 LOAD_DEREF 0 (self)
74 LOAD_ATTR 5 (_loop_ready_evt)
76 POP_JUMP_FORWARD_IF_FALSE 29 (to 96)

78 LOAD_DEREF 0 (self)
80 LOAD_ATTR 5 (_loop_ready_evt)
82 LOAD_METHOD 8 (wait)
84 LOAD_CONST 4 (5)
86 KW_NAMES 5 (('timeout',))
88 CALL 1
90 POP_TOP
92 LOAD_CONST 0 (None)
94 RETURN_VALUE

96 LOAD_CONST 0 (None)
98 RETURN_VALUE

0 COPY_FREE_VARS 1

2 LOAD_GLOBAL 1 (NULL + asyncio)
4 LOAD_ATTR 1 (new_event_loop)
6 CALL 0
8 STORE_FAST 0 (loop)

10 LOAD_GLOBAL 1 (NULL + asyncio)
12 LOAD_ATTR 2 (set_event_loop)
14 LOAD_FAST 0 (loop)
16 CALL 1
18 POP_TOP

20 LOAD_FAST 0 (loop)
22 LOAD_DEREF 1 (self)
24 STORE_ATTR 3 (_loop)

26 NOP

28 LOAD_DEREF 1 (self)
30 LOAD_ATTR 4 (_loop_ready_evt)
32 POP_JUMP_FORWARD_IF_FALSE 25 (to 44)

34 LOAD_DEREF 1 (self)
36 LOAD_ATTR 4 (_loop_ready_evt)
38 LOAD_METHOD 5 (set)
40 CALL 0
42 POP_TOP

44 LOAD_FAST 0 (loop)
46 LOAD_METHOD 6 (run_forever)
48 CALL 0
50 POP_TOP

52 NOP

54 LOAD_FAST 0 (loop)
56 LOAD_METHOD 7 (close)
58 CALL 0
60 POP_TOP
62 LOAD_CONST 0 (None)
64 RETURN_VALUE
66 PUSH_EXC_INFO

68 LOAD_GLOBAL 16 (Exception)
70 CHECK_EXC_MATCH
72 POP_JUMP_FORWARD_IF_FALSE 4 (to 82)
74 POP_TOP

76 POP_EXCEPT
78 LOAD_CONST 0 (None)
80 RETURN_VALUE

82 RERAISE 0
84 COPY 3
86 POP_EXCEPT
88 RERAISE 1
90 PUSH_EXC_INFO

92 NOP

94 LOAD_FAST 0 (loop)
96 LOAD_METHOD 7 (close)
98 CALL 0
100 POP_TOP
102 RERAISE 0
104 PUSH_EXC_INFO

106 LOAD_GLOBAL 16 (Exception)
108 CHECK_EXC_MATCH
110 POP_JUMP_FORWARD_IF_FALSE 3 (to 118)
112 POP_TOP

114 POP_EXCEPT
116 RERAISE 0

118 RERAISE 0
120 COPY 3
122 POP_EXCEPT
124 RERAISE 1
126 COPY 3
128 POP_EXCEPT
130 RERAISE 1


0 LOAD_FAST 0 (self)
2 LOAD_METHOD 0 (_ensure_loop)
4 CALL 0
6 POP_TOP

8 LOAD_FAST 0 (self)
10 LOAD_ATTR 1 (_loop)
12 POP_JUMP_FORWARD_IF_TRUE 15 (to 22)

14 LOAD_GLOBAL 5 (NULL + RuntimeError)
16 LOAD_CONST 1 ("Async loop is not initialized")
18 CALL 1
20 RAISE_VARARGS 1 (exception instance)

22 LOAD_GLOBAL 7 (NULL + asyncio)
24 LOAD_ATTR 4 (run_coroutine_threadsafe)
26 LOAD_FAST 1 (coro)
28 LOAD_FAST 0 (self)
30 LOAD_ATTR 1 (_loop)
32 CALL 2
34 STORE_FAST 2 (fut)

36 LOAD_FAST 2 (fut)
38 LOAD_METHOD 5 (result)
40 CALL 0
42 RETURN_VALUE


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_METHOD 0 (_run_async)
6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_register_account_async)
10 LOAD_FAST 1 (user_data)
12 CALL 1
14 CALL 1
16 RETURN_VALUE
18 PUSH_EXC_INFO

20 LOAD_GLOBAL 4 (Exception)
22 CHECK_EXC_MATCH
24 POP_JUMP_FORWARD_IF_FALSE 57 (to 78)
26 STORE_FAST 2 (e)

28 LOAD_FAST 0 (self)
30 LOAD_ATTR 3 (logger)
32 LOAD_METHOD 4 (error)
34 LOAD_CONST 1 ("Registration error: ")
36 LOAD_FAST 2 (e)
38 FORMAT_VALUE 0
40 BUILD_STRING 2
42 CALL 1
44 POP_TOP

46 LOAD_CONST 2 (False)
48 LOAD_GLOBAL 11 (NULL + str)
50 LOAD_FAST 2 (e)
52 CALL 1
54 LOAD_CONST 3 (('success', 'error'))
56 BUILD_CONST_KEY_MAP 2
58 SWAP 2
60 POP_EXCEPT
62 LOAD_CONST 4 (None)
64 STORE_FAST 2 (e)
66 DELETE_FAST 2 (e)
68 RETURN_VALUE
70 LOAD_CONST 4 (None)
72 STORE_FAST 2 (e)
74 DELETE_FAST 2 (e)
76 RERAISE 1

78 RERAISE 0
80 COPY 3
82 POP_EXCEPT
84 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("INITIALIZATION")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_FAST 0 (self)
22 LOAD_METHOD 2 (_init_browser)
24 CALL 0
26 GET_AWAITABLE 0
28 LOAD_CONST 3 (None)
30 SEND 3 (to 36)
32 YIELD_VALUE
34 JUMP_BACKWARD_NO_INTERRUPT 4 (to 30)
36 POP_TOP

38 LOAD_FAST 0 (self)
40 LOAD_METHOD 3 (_navigate_to_registration)
42 CALL 0
44 GET_AWAITABLE 0
46 LOAD_CONST 3 (None)
48 SEND 3 (to 54)
50 YIELD_VALUE
52 JUMP_BACKWARD_NO_INTERRUPT 4 (to 48)
54 POP_TOP

56 LOAD_FAST 0 (self)
58 LOAD_METHOD 4 (_fill_registration_form)
60 LOAD_FAST 1 (user_data)
62 CALL 1
64 GET_AWAITABLE 0
66 LOAD_CONST 3 (None)
68 SEND 3 (to 74)
70 YIELD_VALUE
72 JUMP_BACKWARD_NO_INTERRUPT 4 (to 68)
74 POP_TOP

76 NOP

78 LOAD_FAST 0 (self)
80 LOAD_METHOD 5 (_scroll_to_recaptcha)
82 LOAD_CONST 4 (3)
84 LOAD_CONST 5 (True)
86 LOAD_CONST 5 (True)
88 KW_NAMES 6 (('max_steps', 'fast', 'skip_fallback'))
90 CALL 3
92 GET_AWAITABLE 0
94 LOAD_CONST 3 (None)
96 SEND 3 (to 102)
98 YIELD_VALUE
100 JUMP_BACKWARD_NO_INTERRUPT 4 (to 96)
102 POP_TOP
104 JUMP_FORWARD 16 (to 128)
106 PUSH_EXC_INFO

108 LOAD_GLOBAL 12 (Exception)
110 CHECK_EXC_MATCH
112 POP_JUMP_FORWARD_IF_FALSE 3 (to 120)
114 POP_TOP

116 POP_EXCEPT
118 JUMP_FORWARD 4 (to 128)

120 RERAISE 0
122 COPY 3
124 POP_EXCEPT
126 RERAISE 1

128 LOAD_FAST 0 (self)
130 LOAD_METHOD 7 (_handle_captcha)
132 CALL 0
134 GET_AWAITABLE 0
136 LOAD_CONST 3 (None)
138 SEND 3 (to 144)
140 YIELD_VALUE
142 JUMP_BACKWARD_NO_INTERRUPT 4 (to 138)
144 STORE_FAST 2 (captcha_ok)

146 LOAD_FAST 2 (captcha_ok)
148 POP_JUMP_FORWARD_IF_TRUE 15 (to 158)

150 LOAD_GLOBAL 13 (NULL + Exception)
152 LOAD_CONST 7 ("Captcha not solved or timed out")
154 CALL 1
156 RAISE_VARARGS 1 (exception instance)

158 LOAD_FAST 0 (self)
160 LOAD_METHOD 8 (_submit_form)
162 CALL 0
164 GET_AWAITABLE 0
166 LOAD_CONST 3 (None)
168 SEND 3 (to 174)
170 YIELD_VALUE
172 JUMP_BACKWARD_NO_INTERRUPT 4 (to 168)
174 POP_TOP

176 LOAD_FAST 0 (self)
178 LOAD_METHOD 9 (_wait_for_result)
180 CALL 0
182 GET_AWAITABLE 0
184 LOAD_CONST 3 (None)
186 SEND 3 (to 192)
188 YIELD_VALUE
190 JUMP_BACKWARD_NO_INTERRUPT 4 (to 186)
192 STORE_FAST 3 (result)

194 LOAD_GLOBAL 1 (NULL + log_automation_step)
196 LOAD_FAST 0 (self)
198 LOAD_ATTR 1 (logger)
200 LOAD_CONST 8 ("REGISTRATION")
202 LOAD_FAST 3 (result)
204 LOAD_CONST 9 ("success")
206 BINARY_SUBSCR
208 POP_JUMP_FORWARD_IF_FALSE 2 (to 214)
210 LOAD_CONST 10 ("SUCCESS")
212 JUMP_FORWARD 1 (to 216)
214 LOAD_CONST 11 ("ERROR")
216 LOAD_FAST 3 (result)
218 CALL 4
220 POP_TOP

222 LOAD_FAST 3 (result)

224 LOAD_FAST 0 (self)
226 LOAD_ATTR 10 (keep_browser_open)
228 POP_JUMP_FORWARD_IF_TRUE 27 (to 250)

230 LOAD_FAST 0 (self)
232 LOAD_METHOD 11 (_cleanup)
234 CALL 0
236 GET_AWAITABLE 0
238 LOAD_CONST 3 (None)
240 SEND 3 (to 246)
242 YIELD_VALUE
244 JUMP_BACKWARD_NO_INTERRUPT 4 (to 240)
246 POP_TOP
248 RETURN_VALUE

250 RETURN_VALUE
252 PUSH_EXC_INFO

254 LOAD_GLOBAL 12 (Exception)
256 CHECK_EXC_MATCH
258 POP_JUMP_FORWARD_IF_FALSE 139 (to 370)
260 STORE_FAST 4 (e)

262 LOAD_GLOBAL 1 (NULL + log_automation_step)
264 LOAD_FAST 0 (self)
266 LOAD_ATTR 1 (logger)
268 LOAD_CONST 8 ("REGISTRATION")
270 LOAD_CONST 11 ("ERROR")
272 LOAD_CONST 12 ("error")
274 LOAD_GLOBAL 25 (NULL + str)
276 LOAD_FAST 4 (e)
278 CALL 1
280 BUILD_MAP 1
282 CALL 4
284 POP_TOP

286 LOAD_CONST 13 (False)
288 LOAD_GLOBAL 25 (NULL + str)
290 LOAD_FAST 4 (e)
292 CALL 1
294 LOAD_GLOBAL 27 (NULL + hasattr)
296 LOAD_FAST 0 (self)
298 LOAD_CONST 14 ("page")
300 CALL 2
302 POP_JUMP_FORWARD_IF_FALSE 22 (to 318)
304 LOAD_GLOBAL 29 (NULL + getattr)
306 LOAD_FAST 0 (self)
308 LOAD_ATTR 15 (page)
310 LOAD_CONST 15 ("url")
312 LOAD_CONST 16 ("N/A")
314 CALL 3
316 JUMP_FORWARD 1 (to 320)
318 LOAD_CONST 16 ("N/A")
320 LOAD_CONST 17 (('success', 'error', 'url'))
322 BUILD_CONST_KEY_MAP 3
324 SWAP 2
326 POP_EXCEPT
328 LOAD_CONST 3 (None)
330 STORE_FAST 4 (e)
332 DELETE_FAST 4 (e)

334 LOAD_FAST 0 (self)
336 LOAD_ATTR 10 (keep_browser_open)
338 POP_JUMP_FORWARD_IF_TRUE 27 (to 360)

340 LOAD_FAST 0 (self)
342 LOAD_METHOD 11 (_cleanup)
344 CALL 0
346 GET_AWAITABLE 0
348 LOAD_CONST 3 (None)
350 SEND 3 (to 356)
352 YIELD_VALUE
354 JUMP_BACKWARD_NO_INTERRUPT 4 (to 350)
356 POP_TOP
358 RETURN_VALUE

360 RETURN_VALUE
362 LOAD_CONST 3 (None)
364 STORE_FAST 4 (e)
366 DELETE_FAST 4 (e)
368 RERAISE 1

370 RERAISE 0
372 COPY 3
374 POP_EXCEPT
376 RERAISE 1
378 PUSH_EXC_INFO

380 LOAD_FAST 0 (self)
382 LOAD_ATTR 10 (keep_browser_open)
384 POP_JUMP_FORWARD_IF_TRUE 27 (to 406)

386 LOAD_FAST 0 (self)
388 LOAD_METHOD 11 (_cleanup)
390 CALL 0
392 GET_AWAITABLE 0
394 LOAD_CONST 3 (None)
396 SEND 3 (to 402)
398 YIELD_VALUE
400 JUMP_BACKWARD_NO_INTERRUPT 4 (to 396)
402 POP_TOP
404 RERAISE 0

406 RERAISE 0
408 COPY 3
410 POP_EXCEPT
412 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 BUILD_LIST 0
8 LOAD_CONST 1 (('successfully confirmed', 'your account was successfully confirmed', 'your account has been confirmed', 'email address has been successfully confirmed'))
10 LIST_EXTEND 1
12 STORE_FAST 1 (success_patterns)

14 BUILD_LIST 0
16 LOAD_CONST 2 (("div[role='alert']", '.alert.alert-success', '.notice', '.flash--success', '#notice', "[class*='success']"))
18 LIST_EXTEND 1
20 STORE_FAST 2 (containers)

22 LOAD_FAST 2 (containers)
24 GET_ITER
26 FOR_ITER 154 (to 176)
28 STORE_FAST 3 (sel)

30 NOP

32 LOAD_FAST 0 (self)
34 LOAD_ATTR 0 (page)
36 LOAD_METHOD 1 (query_selector)
38 LOAD_FAST 3 (sel)
40 CALL 1
42 GET_AWAITABLE 0
44 LOAD_CONST 3 (None)
46 SEND 3 (to 52)
48 YIELD_VALUE
50 JUMP_BACKWARD_NO_INTERRUPT 4 (to 46)
52 STORE_FAST 4 (el)
54 JUMP_FORWARD 18 (to 82)
56 PUSH_EXC_INFO

58 LOAD_GLOBAL 4 (Exception)
60 CHECK_EXC_MATCH
62 POP_JUMP_FORWARD_IF_FALSE 5 (to 74)
64 POP_TOP

66 LOAD_CONST 3 (None)
68 STORE_FAST 4 (el)
70 POP_EXCEPT
72 JUMP_FORWARD 4 (to 82)

74 RERAISE 0
76 COPY 3
78 POP_EXCEPT
80 RERAISE 1

82 LOAD_FAST 4 (el)
84 POP_JUMP_FORWARD_IF_TRUE 1 (to 88)

86 JUMP_BACKWARD 57 (to 26)

88 NOP

90 LOAD_FAST 4 (el)
92 LOAD_METHOD 3 (text_content)
94 CALL 0
96 GET_AWAITABLE 0
98 LOAD_CONST 3 (None)
100 SEND 3 (to 106)
102 YIELD_VALUE
104 JUMP_BACKWARD_NO_INTERRUPT 4 (to 100)
106 JUMP_IF_TRUE_OR_POP 1 (to 110)
108 LOAD_CONST 4 ("")
110 LOAD_METHOD 4 (strip)
112 CALL 0
114 LOAD_METHOD 5 (lower)
116 CALL 0
118 STORE_FAST 5 (txt)
120 JUMP_FORWARD 18 (to 148)
122 PUSH_EXC_INFO

124 LOAD_GLOBAL 4 (Exception)
126 CHECK_EXC_MATCH
128 POP_JUMP_FORWARD_IF_FALSE 5 (to 140)
130 POP_TOP

132 LOAD_CONST 4 ("")
134 STORE_FAST 5 (txt)
136 POP_EXCEPT
138 JUMP_FORWARD 4 (to 148)

140 RERAISE 0
142 COPY 3
144 POP_EXCEPT
146 RERAISE 1

148 LOAD_FAST 1 (success_patterns)
150 GET_ITER
152 FOR_ITER 10 (to 174)
154 STORE_FAST 6 (pat)

156 LOAD_FAST 6 (pat)
158 LOAD_FAST 5 (txt)
160 CONTAINS_OP 0 (in)
162 POP_JUMP_FORWARD_IF_FALSE 4 (to 172)

164 POP_TOP
166 POP_TOP
168 LOAD_CONST 5 (True)
170 RETURN_VALUE

172 JUMP_BACKWARD 11 (to 152)

174 JUMP_BACKWARD 155 (to 26)

176 NOP

178 LOAD_FAST 0 (self)
180 LOAD_ATTR 0 (page)
182 LOAD_METHOD 3 (text_content)
184 LOAD_CONST 6 ("body")
186 CALL 1
188 GET_AWAITABLE 0
190 LOAD_CONST 3 (None)
192 SEND 3 (to 198)
194 YIELD_VALUE
196 JUMP_BACKWARD_NO_INTERRUPT 4 (to 192)
198 JUMP_IF_TRUE_OR_POP 1 (to 202)
200 LOAD_CONST 4 ("")
202 LOAD_METHOD 5 (lower)
204 CALL 0
206 STORE_FAST 7 (body_txt)

208 LOAD_FAST 1 (success_patterns)
210 GET_ITER
212 FOR_ITER 9 (to 232)
214 STORE_FAST 6 (pat)

216 LOAD_FAST 6 (pat)
218 LOAD_FAST 7 (body_txt)
220 CONTAINS_OP 0 (in)
222 POP_JUMP_FORWARD_IF_FALSE 3 (to 230)

224 POP_TOP
226 LOAD_CONST 5 (True)
228 RETURN_VALUE

230 JUMP_BACKWARD 10 (to 212)

232 JUMP_FORWARD 16 (to 256)
234 PUSH_EXC_INFO

236 LOAD_GLOBAL 4 (Exception)
238 CHECK_EXC_MATCH
240 POP_JUMP_FORWARD_IF_FALSE 3 (to 248)
242 POP_TOP

244 POP_EXCEPT
246 JUMP_FORWARD 4 (to 256)

248 RERAISE 0
250 COPY 3
252 POP_EXCEPT
254 RERAISE 1

256 LOAD_CONST 7 (False)
258 RETURN_VALUE
260 PUSH_EXC_INFO

262 LOAD_GLOBAL 4 (Exception)
264 CHECK_EXC_MATCH
266 POP_JUMP_FORWARD_IF_FALSE 4 (to 276)
268 POP_TOP

270 POP_EXCEPT
272 LOAD_CONST 7 (False)
274 RETURN_VALUE

276 RERAISE 0
278 COPY 3
280 POP_EXCEPT
282 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_DEREF 0 (self)
8 LOAD_ATTR 0 (context)
10 POP_JUMP_FORWARD_IF_TRUE 2 (to 16)

12 LOAD_CONST 1 (None)
14 RETURN_VALUE

16 NOP

18 LOAD_DEREF 0 (self)
20 LOAD_ATTR 0 (context)
22 LOAD_METHOD 1 (add_init_script)

24 LOAD_CONST 2 ('\n                    (function(){\n                        try {\n                            // Jangan override di domain Cloud Skills Boost; biarkan popup agar bisa ditangani Playwright\n                            var h = (location && location.hostname) ? location.hostname : \'\';\n                            if (h.includes(\'cloudskillsboost.google\')) {\n                                return;\n                            }\n                        } catch(e) {}\n                        try { window.open = function(u){ try { window.location.href = u; } catch(e) {} return null; }; } catch(e) {}\n                        try {\n                            document.addEventListener(\'click\', function(ev){\n                                const a = ev.target && ev.target.closest ? ev.target.closest(\'a[target="_blank"]\') : null;\n                                if (a && a.href) { try { ev.preventDefault(); window.location.href = a.href; } catch(e){} }\n                            }, true);\n                        } catch(e) {}\n                    })();\n                    ')
26 CALL 1
28 GET_AWAITABLE 0
30 LOAD_CONST 1 (None)
32 SEND 3 (to 38)
34 YIELD_VALUE
36 JUMP_BACKWARD_NO_INTERRUPT 4 (to 32)
38 POP_TOP
40 JUMP_FORWARD 16 (to 64)
42 PUSH_EXC_INFO

44 LOAD_GLOBAL 4 (Exception)
46 CHECK_EXC_MATCH
48 POP_JUMP_FORWARD_IF_FALSE 3 (to 56)
50 POP_TOP

52 POP_EXCEPT
54 JUMP_FORWARD 4 (to 64)

56 RERAISE 0
58 COPY 3
60 POP_EXCEPT
62 RERAISE 1

64 NOP

66 LOAD_CLOSURE 0 (self)
68 BUILD_TUPLE 1
70 LOAD_CONST 3 (code object _handler)
72 MAKE_FUNCTION 8 (closure)
74 STORE_DEREF 1 (self)

76 LOAD_DEREF 0 (self)
78 LOAD_ATTR 0 (context)
80 LOAD_METHOD 3 (remove_listeners)
82 LOAD_CONST 4 ("page")
84 CALL 1
86 POP_TOP

88 LOAD_DEREF 0 (self)
90 LOAD_ATTR 0 (context)
92 LOAD_METHOD 4 (on)
94 LOAD_CONST 4 ("page")
96 LOAD_CLOSURE 1 (self)
98 BUILD_TUPLE 1
100 LOAD_CONST 5 (code object <lambda>)
102 MAKE_FUNCTION 8 (closure)
104 CALL 2
106 POP_TOP
108 LOAD_CONST 1 (None)
110 RETURN_VALUE
112 PUSH_EXC_INFO

114 LOAD_GLOBAL 4 (Exception)
116 CHECK_EXC_MATCH
118 POP_JUMP_FORWARD_IF_FALSE 4 (to 128)
120 POP_TOP

122 POP_EXCEPT
124 LOAD_CONST 1 (None)
126 RETURN_VALUE

128 RERAISE 0
130 COPY 3
132 POP_EXCEPT
134 RERAISE 1
136 PUSH_EXC_INFO

138 LOAD_GLOBAL 4 (Exception)
140 CHECK_EXC_MATCH
142 POP_JUMP_FORWARD_IF_FALSE 4 (to 152)
144 POP_TOP

146 POP_EXCEPT
148 LOAD_CONST 1 (None)
150 RETURN_VALUE

152 RERAISE 0
154 COPY 3
156 POP_EXCEPT
158 RERAISE 1

0 COPY_FREE_VARS 1

2 RETURN_GENERATOR
4 POP_TOP

6 NOP

8 LOAD_CONST 0 (None)
10 STORE_FAST 1 (target_url)

12 LOAD_GLOBAL 1 (NULL + range)
14 LOAD_CONST 1 (20)
16 CALL 1
18 GET_ITER
20 FOR_ITER 67 (to 102)
22 STORE_FAST 2 (_)

24 NOP

26 LOAD_FAST 0 (p)
28 LOAD_ATTR 1 (url)
30 STORE_FAST 3 (u)
32 JUMP_FORWARD 18 (to 60)
34 PUSH_EXC_INFO

36 LOAD_GLOBAL 4 (Exception)
38 CHECK_EXC_MATCH
40 POP_JUMP_FORWARD_IF_FALSE 5 (to 52)
42 POP_TOP

44 LOAD_CONST 2 ("")
46 STORE_FAST 3 (u)
48 POP_EXCEPT
50 JUMP_FORWARD 4 (to 60)

52 RERAISE 0
54 COPY 3
56 POP_EXCEPT
58 RERAISE 1

60 LOAD_FAST 3 (u)
62 POP_JUMP_FORWARD_IF_FALSE 10 (to 80)
64 LOAD_FAST 3 (u)
66 LOAD_CONST 3 ("about:blank")
68 COMPARE_OP 3 (!=)
70 POP_JUMP_FORWARD_IF_FALSE 4 (to 80)

72 LOAD_FAST 3 (u)
74 STORE_FAST 1 (target_url)

76 POP_TOP
78 JUMP_FORWARD 27 (to 102)

80 LOAD_GLOBAL 7 (NULL + asyncio)
82 LOAD_ATTR 4 (sleep)
84 LOAD_CONST 4 (0.1)
86 CALL 1
88 GET_AWAITABLE 0
90 LOAD_CONST 0 (None)
92 SEND 3 (to 98)
94 YIELD_VALUE
96 JUMP_BACKWARD_NO_INTERRUPT 4 (to 92)
98 POP_TOP
100 JUMP_BACKWARD 68 (to 20)

102 LOAD_FAST 1 (target_url)
104 POP_JUMP_FORWARD_IF_TRUE 54 (to 162)

106 NOP

108 LOAD_FAST 0 (p)
110 LOAD_METHOD 5 (wait_for_load_state)
112 LOAD_CONST 5 ("domcontentloaded")
114 LOAD_CONST 6 (3000)
116 KW_NAMES 7 (('timeout',))
118 CALL 2
120 GET_AWAITABLE 0
122 LOAD_CONST 0 (None)
124 SEND 3 (to 130)
126 YIELD_VALUE
128 JUMP_BACKWARD_NO_INTERRUPT 4 (to 124)
130 POP_TOP

132 LOAD_FAST 0 (p)
134 LOAD_ATTR 1 (url)
136 STORE_FAST 1 (target_url)
138 JUMP_FORWARD 16 (to 162)
140 PUSH_EXC_INFO

142 LOAD_GLOBAL 4 (Exception)
144 CHECK_EXC_MATCH
146 POP_JUMP_FORWARD_IF_FALSE 3 (to 154)
148 POP_TOP

150 POP_EXCEPT
152 JUMP_FORWARD 4 (to 162)

154 RERAISE 0
156 COPY 3
158 POP_EXCEPT
160 RERAISE 1

162 LOAD_GLOBAL 13 (NULL + getattr)
164 LOAD_DEREF 7 (self)
166 LOAD_CONST 8 ("_popup_mode")
168 LOAD_CONST 9 ("redirect")
170 CALL 3
172 STORE_FAST 4 (mode)

174 LOAD_FAST 4 (mode)
176 LOAD_CONST 10 ("switch")
178 COMPARE_OP 2 (==)
180 POP_JUMP_FORWARD_IF_FALSE 254 (to 440)

182 NOP

184 LOAD_FAST 1 (target_url)
186 JUMP_IF_FALSE_OR_POP 21 (to 198)
188 LOAD_FAST 1 (target_url)
190 LOAD_METHOD 7 (startswith)
192 LOAD_CONST 3 ("about:blank")
194 CALL 1
196 UNARY_NOT
198 STORE_FAST 5 (valid_url)

200 LOAD_FAST 5 (valid_url)
202 POP_JUMP_FORWARD_IF_TRUE 100 (to 300)

204 LOAD_GLOBAL 1 (NULL + range)
206 LOAD_CONST 11 (25)
208 CALL 1
210 GET_ITER
212 FOR_ITER 84 (to 300)
214 STORE_FAST 2 (_)

216 NOP

218 LOAD_GLOBAL 7 (NULL + asyncio)
220 LOAD_ATTR 4 (sleep)
222 LOAD_CONST 12 (0.2)
224 CALL 1
226 GET_AWAITABLE 0
228 LOAD_CONST 0 (None)
230 SEND 3 (to 236)
232 YIELD_VALUE
234 JUMP_BACKWARD_NO_INTERRUPT 4 (to 230)
236 POP_TOP

238 LOAD_FAST 0 (p)
240 LOAD_ATTR 1 (url)
242 STORE_FAST 6 (cur)
244 JUMP_FORWARD 18 (to 272)
246 PUSH_EXC_INFO

248 LOAD_GLOBAL 4 (Exception)
250 CHECK_EXC_MATCH
252 POP_JUMP_FORWARD_IF_FALSE 5 (to 264)
254 POP_TOP

256 LOAD_CONST 2 ("")
258 STORE_FAST 6 (cur)
260 POP_EXCEPT
262 JUMP_FORWARD 4 (to 272)

264 RERAISE 0
266 COPY 3
268 POP_EXCEPT
270 RERAISE 1

272 LOAD_FAST 6 (cur)
274 POP_JUMP_FORWARD_IF_FALSE 27 (to 298)
276 LOAD_FAST 6 (cur)
278 LOAD_METHOD 7 (startswith)
280 LOAD_CONST 3 ("about:blank")
282 CALL 1
284 POP_JUMP_FORWARD_IF_TRUE 6 (to 298)

286 LOAD_FAST 6 (cur)
288 STORE_FAST 1 (target_url)

290 LOAD_CONST 13 (True)
292 STORE_FAST 5 (valid_url)

294 POP_TOP
296 JUMP_FORWARD 1 (to 300)
298 JUMP_BACKWARD 85 (to 212)

300 LOAD_FAST 5 (valid_url)
302 POP_JUMP_FORWARD_IF_FALSE 56 (to 356)

304 LOAD_FAST 0 (p)
306 LOAD_DEREF 7 (self)
308 STORE_ATTR 8 (page)

310 NOP

312 LOAD_DEREF 7 (self)
314 LOAD_ATTR 8 (page)
316 LOAD_METHOD 9 (bring_to_front)
318 CALL 0
320 GET_AWAITABLE 0
322 LOAD_CONST 0 (None)
324 SEND 3 (to 330)
326 YIELD_VALUE
328 JUMP_BACKWARD_NO_INTERRUPT 4 (to 324)
330 POP_TOP
332 JUMP_FORWARD 60 (to 400)
334 PUSH_EXC_INFO

336 LOAD_GLOBAL 4 (Exception)
338 CHECK_EXC_MATCH
340 POP_JUMP_FORWARD_IF_FALSE 3 (to 348)
342 POP_TOP

344 POP_EXCEPT
346 JUMP_FORWARD 50 (to 404)

348 RERAISE 0
350 COPY 3
352 POP_EXCEPT
354 RERAISE 1

356 NOP

358 LOAD_FAST 0 (p)
360 LOAD_METHOD 10 (close)
362 CALL 0
364 GET_AWAITABLE 0
366 LOAD_CONST 0 (None)
368 SEND 3 (to 374)
370 YIELD_VALUE
372 JUMP_BACKWARD_NO_INTERRUPT 4 (to 368)
374 POP_TOP
376 JUMP_FORWARD 20 (to 408)
378 PUSH_EXC_INFO

380 LOAD_GLOBAL 4 (Exception)
382 CHECK_EXC_MATCH
384 POP_JUMP_FORWARD_IF_FALSE 3 (to 392)
386 POP_TOP

388 POP_EXCEPT
390 JUMP_FORWARD 10 (to 412)

392 RERAISE 0
394 COPY 3
396 POP_EXCEPT
398 RERAISE 1

400 LOAD_CONST 0 (None)
402 RETURN_VALUE

404 LOAD_CONST 0 (None)
406 RETURN_VALUE

408 LOAD_CONST 0 (None)
410 RETURN_VALUE

412 LOAD_CONST 0 (None)
414 RETURN_VALUE
416 PUSH_EXC_INFO

418 LOAD_GLOBAL 4 (Exception)
420 CHECK_EXC_MATCH
422 POP_JUMP_FORWARD_IF_FALSE 4 (to 432)
424 POP_TOP

426 POP_EXCEPT
428 LOAD_CONST 0 (None)
430 RETURN_VALUE

432 RERAISE 0
434 COPY 3
436 POP_EXCEPT
438 RERAISE 1

440 LOAD_FAST 4 (mode)
442 LOAD_CONST 14 ("ignore")
444 COMPARE_OP 2 (==)
446 POP_JUMP_FORWARD_IF_FALSE 46 (to 496)

448 NOP

450 LOAD_FAST 0 (p)
452 LOAD_METHOD 10 (close)
454 CALL 0
456 GET_AWAITABLE 0
458 LOAD_CONST 0 (None)
460 SEND 3 (to 466)
462 YIELD_VALUE
464 JUMP_BACKWARD_NO_INTERRUPT 4 (to 460)
466 POP_TOP
468 LOAD_CONST 0 (None)
470 RETURN_VALUE
472 PUSH_EXC_INFO

474 LOAD_GLOBAL 4 (Exception)
476 CHECK_EXC_MATCH
478 POP_JUMP_FORWARD_IF_FALSE 4 (to 488)
480 POP_TOP

482 POP_EXCEPT
484 LOAD_CONST 0 (None)
486 RETURN_VALUE

488 RERAISE 0
490 COPY 3
492 POP_EXCEPT
494 RERAISE 1

496 LOAD_DEREF 7 (self)
498 LOAD_ATTR 8 (page)
500 POP_JUMP_FORWARD_IF_FALSE 73 (to 564)
502 LOAD_FAST 1 (target_url)
504 POP_JUMP_FORWARD_IF_FALSE 71 (to 564)
506 LOAD_FAST 1 (target_url)
508 LOAD_METHOD 7 (startswith)
510 LOAD_CONST 3 ("about:blank")
512 CALL 1
514 POP_JUMP_FORWARD_IF_TRUE 50 (to 564)

516 NOP

518 LOAD_DEREF 7 (self)
520 LOAD_ATTR 8 (page)
522 LOAD_METHOD 11 (goto)
524 LOAD_FAST 1 (target_url)
526 CALL 1
528 GET_AWAITABLE 0
530 LOAD_CONST 0 (None)
532 SEND 3 (to 538)
534 YIELD_VALUE
536 JUMP_BACKWARD_NO_INTERRUPT 4 (to 532)
538 POP_TOP
540 JUMP_FORWARD 16 (to 564)
542 PUSH_EXC_INFO

544 LOAD_GLOBAL 4 (Exception)
546 CHECK_EXC_MATCH
548 POP_JUMP_FORWARD_IF_FALSE 3 (to 556)
550 POP_TOP

552 POP_EXCEPT
554 JUMP_FORWARD 4 (to 564)

556 RERAISE 0
558 COPY 3
560 POP_EXCEPT
562 RERAISE 1

564 NOP

566 LOAD_FAST 0 (p)
568 LOAD_METHOD 10 (close)
570 CALL 0
572 GET_AWAITABLE 0
574 LOAD_CONST 0 (None)
576 SEND 3 (to 582)
578 YIELD_VALUE
580 JUMP_BACKWARD_NO_INTERRUPT 4 (to 576)
582 POP_TOP
584 LOAD_CONST 0 (None)
586 RETURN_VALUE
588 PUSH_EXC_INFO

590 LOAD_GLOBAL 4 (Exception)
592 CHECK_EXC_MATCH
594 POP_JUMP_FORWARD_IF_FALSE 4 (to 604)
596 POP_TOP

598 POP_EXCEPT
600 LOAD_CONST 0 (None)
602 RETURN_VALUE

604 RERAISE 0
606 COPY 3
608 POP_EXCEPT
610 RERAISE 1
612 PUSH_EXC_INFO

614 LOAD_GLOBAL 4 (Exception)
616 CHECK_EXC_MATCH
618 POP_JUMP_FORWARD_IF_FALSE 4 (to 628)
620 POP_TOP

622 POP_EXCEPT
624 LOAD_CONST 0 (None)
626 RETURN_VALUE

628 RERAISE 0
630 COPY 3
632 POP_EXCEPT
634 RERAISE 1

0 COPY_FREE_VARS 1

2 LOAD_GLOBAL 1 (NULL + asyncio)
4 LOAD_ATTR 1 (create_task)
6 PUSH_NULL
8 LOAD_DEREF 1 (_handler)
10 LOAD_FAST 0 (p)
12 CALL 1
14 CALL 1
16 RETURN_VALUE


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_FAST 0 (self)
8 LOAD_ATTR 0 (context)
10 POP_JUMP_FORWARD_IF_FALSE 28 (to 28)

12 LOAD_FAST 0 (self)
14 LOAD_ATTR 0 (context)
16 LOAD_METHOD 1 (remove_listeners)
18 LOAD_CONST 1 ("page")
20 CALL 1
22 POP_TOP
24 LOAD_CONST 2 (None)
26 RETURN_VALUE

28 LOAD_CONST 2 (None)
30 RETURN_VALUE
32 PUSH_EXC_INFO

34 LOAD_GLOBAL 4 (Exception)
36 CHECK_EXC_MATCH
38 POP_JUMP_FORWARD_IF_FALSE 4 (to 48)
40 POP_TOP

42 POP_EXCEPT
44 LOAD_CONST 2 (None)
46 RETURN_VALUE

48 RERAISE 0
50 COPY 3
52 POP_EXCEPT
54 RERAISE 1


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_METHOD 0 (_run_async)
6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_confirm_via_link_async)
10 LOAD_FAST 1 (url)
12 LOAD_FAST 2 (password)
14 LOAD_FAST 3 (email)
16 CALL 3
18 CALL 1
20 RETURN_VALUE
22 PUSH_EXC_INFO

24 LOAD_GLOBAL 4 (Exception)
26 CHECK_EXC_MATCH
28 POP_JUMP_FORWARD_IF_FALSE 57 (to 82)
30 STORE_FAST 4 (e)

32 LOAD_FAST 0 (self)
34 LOAD_ATTR 3 (logger)
36 LOAD_METHOD 4 (error)
38 LOAD_CONST 1 ("Confirm via link error: ")
40 LOAD_FAST 4 (e)
42 FORMAT_VALUE 0
44 BUILD_STRING 2
46 CALL 1
48 POP_TOP

50 LOAD_CONST 2 (False)
52 LOAD_GLOBAL 11 (NULL + str)
54 LOAD_FAST 4 (e)
56 CALL 1
58 LOAD_CONST 3 (('success', 'error'))
60 BUILD_CONST_KEY_MAP 2
62 SWAP 2
64 POP_EXCEPT
66 LOAD_CONST 4 (None)
68 STORE_FAST 4 (e)
70 DELETE_FAST 4 (e)
72 RETURN_VALUE
74 LOAD_CONST 4 (None)
76 STORE_FAST 4 (e)
78 DELETE_FAST 4 (e)
80 RERAISE 1

82 RERAISE 0
84 COPY 3
86 POP_EXCEPT
88 RERAISE 1


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_METHOD 0 (_run_async)
6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_start_lab_async)
10 LOAD_FAST 1 (lab_url)
12 CALL 1
14 CALL 1
16 RETURN_VALUE
18 PUSH_EXC_INFO

20 LOAD_GLOBAL 4 (Exception)
22 CHECK_EXC_MATCH
24 POP_JUMP_FORWARD_IF_FALSE 66 (to 84)
26 STORE_FAST 2 (e)

28 LOAD_GLOBAL 7 (NULL + log_automation_step)
30 LOAD_FAST 0 (self)
32 LOAD_ATTR 4 (logger)
34 LOAD_CONST 1 ("LAB_START")
36 LOAD_CONST 2 ("ERROR")
38 LOAD_CONST 3 ("error")
40 LOAD_GLOBAL 11 (NULL + str)
42 LOAD_FAST 2 (e)
44 CALL 1
46 BUILD_MAP 1
48 CALL 4
50 POP_TOP

52 LOAD_CONST 4 (False)
54 LOAD_GLOBAL 11 (NULL + str)
56 LOAD_FAST 2 (e)
58 CALL 1
60 LOAD_CONST 5 (('success', 'error'))
62 BUILD_CONST_KEY_MAP 2
64 SWAP 2
66 POP_EXCEPT
68 LOAD_CONST 6 (None)
70 STORE_FAST 2 (e)
72 DELETE_FAST 2 (e)
74 RETURN_VALUE
76 LOAD_CONST 6 (None)
78 STORE_FAST 2 (e)
80 DELETE_FAST 2 (e)
82 RERAISE 1

84 RERAISE 0
86 COPY 3
88 POP_EXCEPT
90 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_DEREF 0 (self)
6 LOAD_ATTR 0 (page)
8 POP_JUMP_FORWARD_IF_TRUE 15 (to 18)

10 LOAD_GLOBAL 3 (NULL + RuntimeError)
12 LOAD_CONST 1 ("Page is not initialized")
14 CALL 1
16 RAISE_VARARGS 1 (exception instance)

18 NOP

20 LOAD_DEREF 0 (self)
22 LOAD_ATTR 2 (_popup_mode)
24 STORE_FAST 2 (prev_mode)

26 LOAD_CONST 2 ("ignore")
28 LOAD_DEREF 0 (self)
30 STORE_ATTR 2 (_popup_mode)

32 NOP

34 LOAD_DEREF 0 (self)
36 LOAD_METHOD 3 (_unbind_page_policy)
38 CALL 0
40 GET_AWAITABLE 0
42 LOAD_CONST 3 (None)
44 SEND 3 (to 50)
46 YIELD_VALUE
48 JUMP_BACKWARD_NO_INTERRUPT 4 (to 44)
50 POP_TOP
52 JUMP_FORWARD 16 (to 76)
54 PUSH_EXC_INFO

56 LOAD_GLOBAL 8 (Exception)
58 CHECK_EXC_MATCH
60 POP_JUMP_FORWARD_IF_FALSE 3 (to 68)
62 POP_TOP

64 POP_EXCEPT
66 JUMP_FORWARD 4 (to 76)

68 RERAISE 0
70 COPY 3
72 POP_EXCEPT
74 RERAISE 1

76 LOAD_GLOBAL 11 (NULL + start_lab_action)

78 LOAD_DEREF 0 (self)
80 LOAD_ATTR 0 (page)

82 LOAD_DEREF 0 (self)
84 LOAD_ATTR 6 (logger)

86 LOAD_CLOSURE 0 (self)
88 BUILD_TUPLE 1
90 LOAD_CONST 4 (code object <lambda>)
92 MAKE_FUNCTION 8 (closure)

94 LOAD_FAST 1 (lab_url)

96 LOAD_CONST 5 (True)

98 KW_NAMES 6 (('page', 'logger', 'handle_captcha', 'lab_url', 'wait_networkidle'))
100 CALL 5
102 GET_AWAITABLE 0
104 LOAD_CONST 3 (None)
106 SEND 3 (to 112)
108 YIELD_VALUE
110 JUMP_BACKWARD_NO_INTERRUPT 4 (to 106)
112 STORE_FAST 3 (result)

114 LOAD_FAST 3 (result)
116 LOAD_METHOD 7 (get)
118 LOAD_CONST 7 ("success")
120 CALL 1
122 POP_JUMP_FORWARD_IF_TRUE 52 (to 176)

124 LOAD_FAST 3 (result)

126 LOAD_FAST 2 (prev_mode)
128 LOAD_DEREF 0 (self)
130 STORE_ATTR 2 (_popup_mode)

132 NOP

134 LOAD_DEREF 0 (self)
136 LOAD_METHOD 8 (_bind_single_page_policy)
138 CALL 0
140 GET_AWAITABLE 0
142 LOAD_CONST 3 (None)
144 SEND 3 (to 150)
146 YIELD_VALUE
148 JUMP_BACKWARD_NO_INTERRUPT 4 (to 144)
150 POP_TOP
152 RETURN_VALUE
154 PUSH_EXC_INFO

156 LOAD_GLOBAL 8 (Exception)
158 CHECK_EXC_MATCH
160 POP_JUMP_FORWARD_IF_FALSE 3 (to 168)
162 POP_TOP

164 POP_EXCEPT
166 RETURN_VALUE

168 RERAISE 0
170 COPY 3
172 POP_EXCEPT
174 RERAISE 1

176 LOAD_CONST 3 (None)
178 STORE_FAST 4 (inc_ctx)

180 LOAD_CONST 3 (None)
182 STORE_FAST 5 (inc_page)

184 NOP

186 LOAD_DEREF 0 (self)
188 LOAD_ATTR 9 (browser)
190 POP_JUMP_FORWARD_IF_TRUE 108 (to 304)

192 LOAD_CONST 8 (False)
194 LOAD_CONST 9 ("Browser not initialized")
196 LOAD_CONST 10 (('success', 'error'))
198 BUILD_CONST_KEY_MAP 2

200 NOP

202 LOAD_FAST 4 (inc_ctx)
204 POP_JUMP_FORWARD_IF_FALSE 33 (to 230)
206 LOAD_DEREF 0 (self)
208 LOAD_ATTR 10 (keep_browser_open)
210 POP_JUMP_FORWARD_IF_TRUE 26 (to 230)

212 LOAD_FAST 4 (inc_ctx)
214 LOAD_METHOD 11 (close)
216 CALL 0
218 GET_AWAITABLE 0
220 LOAD_CONST 3 (None)
222 SEND 3 (to 228)
224 YIELD_VALUE
226 JUMP_BACKWARD_NO_INTERRUPT 4 (to 222)
228 POP_TOP
230 JUMP_FORWARD 16 (to 254)
232 PUSH_EXC_INFO

234 LOAD_GLOBAL 8 (Exception)
236 CHECK_EXC_MATCH
238 POP_JUMP_FORWARD_IF_FALSE 3 (to 246)
240 POP_TOP

242 POP_EXCEPT
244 JUMP_FORWARD 4 (to 254)

246 RERAISE 0
248 COPY 3
250 POP_EXCEPT
252 RERAISE 1

254 LOAD_FAST 2 (prev_mode)
256 LOAD_DEREF 0 (self)
258 STORE_ATTR 2 (_popup_mode)

260 NOP

262 LOAD_DEREF 0 (self)
264 LOAD_METHOD 8 (_bind_single_page_policy)
266 CALL 0
268 GET_AWAITABLE 0
270 LOAD_CONST 3 (None)
272 SEND 3 (to 278)
274 YIELD_VALUE
276 JUMP_BACKWARD_NO_INTERRUPT 4 (to 272)
278 POP_TOP
280 RETURN_VALUE
282 PUSH_EXC_INFO

284 LOAD_GLOBAL 8 (Exception)
286 CHECK_EXC_MATCH
288 POP_JUMP_FORWARD_IF_FALSE 3 (to 296)
290 POP_TOP

292 POP_EXCEPT
294 RETURN_VALUE

296 RERAISE 0
298 COPY 3
300 POP_EXCEPT
302 RERAISE 1

304 LOAD_GLOBAL 25 (NULL + open_console_action)
306 LOAD_DEREF 0 (self)
308 LOAD_ATTR 0 (page)
310 LOAD_DEREF 0 (self)
312 LOAD_ATTR 6 (logger)
314 LOAD_DEREF 0 (self)
316 LOAD_ATTR 9 (browser)
318 LOAD_CONST 11 (300)
320 KW_NAMES 12 (('timeout_sec',))
322 CALL 4
324 GET_AWAITABLE 0
326 LOAD_CONST 3 (None)
328 SEND 3 (to 334)
330 YIELD_VALUE
332 JUMP_BACKWARD_NO_INTERRUPT 4 (to 328)
334 UNPACK_SEQUENCE 3
336 STORE_FAST 6 (console_info)
338 STORE_FAST 4 (inc_ctx)
340 STORE_FAST 5 (inc_page)

342 LOAD_FAST 6 (console_info)
344 LOAD_METHOD 7 (get)
346 LOAD_CONST 13 ("opened")
348 CALL 1
350 POP_JUMP_FORWARD_IF_FALSE 2 (to 356)
352 LOAD_FAST 5 (inc_page)
354 POP_JUMP_FORWARD_IF_TRUE 151 (to 494)

356 LOAD_GLOBAL 27 (NULL + log_automation_step)
358 LOAD_DEREF 0 (self)
360 LOAD_ATTR 6 (logger)
362 LOAD_CONST 14 ("OPEN_CONSOLE")
364 LOAD_CONST 15 ("FAILED")
366 CALL 3
368 POP_TOP

370 LOAD_CONST 8 (False)

372 LOAD_CONST 16 ("Could not open Google Cloud console")
374 LOAD_GLOBAL 29 (NULL + getattr)
376 LOAD_DEREF 0 (self)
378 LOAD_ATTR 0 (page)
380 LOAD_CONST 17 ("url")
382 LOAD_CONST 18 ("")
384 CALL 3

386 LOAD_CONST 19 (('success', 'error', 'url'))
388 BUILD_CONST_KEY_MAP 3

390 NOP

392 LOAD_FAST 4 (inc_ctx)
394 POP_JUMP_FORWARD_IF_FALSE 33 (to 420)
396 LOAD_DEREF 0 (self)
398 LOAD_ATTR 10 (keep_browser_open)
400 POP_JUMP_FORWARD_IF_TRUE 26 (to 420)

402 LOAD_FAST 4 (inc_ctx)
404 LOAD_METHOD 11 (close)
406 CALL 0
408 GET_AWAITABLE 0
410 LOAD_CONST 3 (None)
412 SEND 3 (to 418)
414 YIELD_VALUE
416 JUMP_BACKWARD_NO_INTERRUPT 4 (to 412)
418 POP_TOP
420 JUMP_FORWARD 16 (to 444)
422 PUSH_EXC_INFO

424 LOAD_GLOBAL 8 (Exception)
426 CHECK_EXC_MATCH
428 POP_JUMP_FORWARD_IF_FALSE 3 (to 436)
430 POP_TOP

432 POP_EXCEPT
434 JUMP_FORWARD 4 (to 444)

436 RERAISE 0
438 COPY 3
440 POP_EXCEPT
442 RERAISE 1

444 LOAD_FAST 2 (prev_mode)
446 LOAD_DEREF 0 (self)
448 STORE_ATTR 2 (_popup_mode)

450 NOP

452 LOAD_DEREF 0 (self)
454 LOAD_METHOD 8 (_bind_single_page_policy)
456 CALL 0
458 GET_AWAITABLE 0
460 LOAD_CONST 3 (None)
462 SEND 3 (to 468)
464 YIELD_VALUE
466 JUMP_BACKWARD_NO_INTERRUPT 4 (to 462)
468 POP_TOP
470 RETURN_VALUE
472 PUSH_EXC_INFO

474 LOAD_GLOBAL 8 (Exception)
476 CHECK_EXC_MATCH
478 POP_JUMP_FORWARD_IF_FALSE 3 (to 486)
480 POP_TOP

482 POP_EXCEPT
484 RETURN_VALUE

486 RERAISE 0
488 COPY 3
490 POP_EXCEPT
492 RERAISE 1

494 LOAD_GLOBAL 31 (NULL + handle_terms_action)
496 LOAD_FAST 5 (inc_page)
498 LOAD_DEREF 0 (self)
500 LOAD_ATTR 6 (logger)
502 LOAD_CONST 20 (120)
504 KW_NAMES 12 (('timeout_sec',))
506 CALL 3
508 GET_AWAITABLE 0
510 LOAD_CONST 3 (None)
512 SEND 3 (to 518)
514 YIELD_VALUE
516 JUMP_BACKWARD_NO_INTERRUPT 4 (to 512)
518 STORE_FAST 7 (terms_res)

520 LOAD_FAST 7 (terms_res)
522 LOAD_METHOD 7 (get)
524 LOAD_CONST 21 ("handled")
526 CALL 1
528 POP_JUMP_FORWARD_IF_TRUE 46 (to 560)

530 LOAD_GLOBAL 27 (NULL + log_automation_step)
532 LOAD_DEREF 0 (self)
534 LOAD_ATTR 6 (logger)
536 LOAD_CONST 22 ("TERMS")
538 LOAD_CONST 23 ("SKIPPED_OR_FAILED")
540 LOAD_CONST 24 ("reason")
542 LOAD_FAST 7 (terms_res)
544 LOAD_METHOD 7 (get)
546 LOAD_CONST 24 ("reason")
548 LOAD_CONST 18 ("")
550 CALL 2
552 BUILD_MAP 1
554 CALL 4
556 POP_TOP
558 JUMP_FORWARD 45 (to 588)

560 LOAD_GLOBAL 27 (NULL + log_automation_step)
562 LOAD_DEREF 0 (self)
564 LOAD_ATTR 6 (logger)
566 LOAD_CONST 22 ("TERMS")
568 LOAD_CONST 25 ("DONE")
570 LOAD_CONST 17 ("url")
572 LOAD_FAST 7 (terms_res)
574 LOAD_METHOD 7 (get)
576 LOAD_CONST 17 ("url")
578 LOAD_CONST 18 ("")
580 CALL 2
582 BUILD_MAP 1
584 CALL 4
586 POP_TOP

588 LOAD_CONST 18 ("")
590 STORE_FAST 8 (project_id)

592 NOP

594 LOAD_GLOBAL 33 (NULL + parse_qs)
596 LOAD_GLOBAL 35 (NULL + urlparse)
598 LOAD_FAST 5 (inc_page)
600 LOAD_ATTR 18 (url)
602 CALL 1
604 LOAD_ATTR 19 (query)
606 CALL 1
608 STORE_FAST 9 (q)

610 LOAD_FAST 9 (q)
612 LOAD_METHOD 7 (get)
614 LOAD_CONST 26 ("project")
616 LOAD_CONST 18 ("")
618 BUILD_LIST 1
620 CALL 2
622 JUMP_IF_TRUE_OR_POP 2 (to 628)
624 LOAD_CONST 18 ("")
626 BUILD_LIST 1
628 LOAD_CONST 27 (0)
630 BINARY_SUBSCR
632 STORE_FAST 8 (project_id)
634 JUMP_FORWARD 18 (to 662)
636 PUSH_EXC_INFO

638 LOAD_GLOBAL 8 (Exception)
640 CHECK_EXC_MATCH
642 POP_JUMP_FORWARD_IF_FALSE 5 (to 654)
644 POP_TOP

646 LOAD_CONST 18 ("")
648 STORE_FAST 8 (project_id)
650 POP_EXCEPT
652 JUMP_FORWARD 4 (to 662)

654 RERAISE 0
656 COPY 3
658 POP_EXCEPT
660 RERAISE 1

662 LOAD_FAST 8 (project_id)
664 POP_JUMP_FORWARD_IF_TRUE 133 (to 798)

666 LOAD_CONST 8 (False)

668 LOAD_CONST 28 ("Could not parse project_id from console URL")
670 LOAD_CONST 5 (True)

672 LOAD_GLOBAL 41 (NULL + hasattr)
674 LOAD_FAST 5 (inc_page)
676 LOAD_CONST 17 ("url")
678 CALL 2
680 POP_JUMP_FORWARD_IF_FALSE 7 (to 688)
682 LOAD_FAST 5 (inc_page)
684 LOAD_ATTR 18 (url)
686 JUMP_FORWARD 1 (to 690)

688 LOAD_CONST 18 ("")
690 LOAD_CONST 29 (('success', 'error', 'console_opened', 'console_url'))
692 BUILD_CONST_KEY_MAP 4

694 NOP

696 LOAD_FAST 4 (inc_ctx)
698 POP_JUMP_FORWARD_IF_FALSE 33 (to 724)
700 LOAD_DEREF 0 (self)
702 LOAD_ATTR 10 (keep_browser_open)
704 POP_JUMP_FORWARD_IF_TRUE 26 (to 724)

706 LOAD_FAST 4 (inc_ctx)
708 LOAD_METHOD 11 (close)
710 CALL 0
712 GET_AWAITABLE 0
714 LOAD_CONST 3 (None)
716 SEND 3 (to 722)
718 YIELD_VALUE
720 JUMP_BACKWARD_NO_INTERRUPT 4 (to 716)
722 POP_TOP
724 JUMP_FORWARD 16 (to 748)
726 PUSH_EXC_INFO

728 LOAD_GLOBAL 8 (Exception)
730 CHECK_EXC_MATCH
732 POP_JUMP_FORWARD_IF_FALSE 3 (to 740)
734 POP_TOP

736 POP_EXCEPT
738 JUMP_FORWARD 4 (to 748)

740 RERAISE 0
742 COPY 3
744 POP_EXCEPT
746 RERAISE 1

748 LOAD_FAST 2 (prev_mode)
750 LOAD_DEREF 0 (self)
752 STORE_ATTR 2 (_popup_mode)

754 NOP

756 LOAD_DEREF 0 (self)
758 LOAD_METHOD 8 (_bind_single_page_policy)
760 CALL 0
762 GET_AWAITABLE 0
764 LOAD_CONST 3 (None)
766 SEND 3 (to 772)
768 YIELD_VALUE
770 JUMP_BACKWARD_NO_INTERRUPT 4 (to 766)
772 POP_TOP
774 RETURN_VALUE
776 PUSH_EXC_INFO

778 LOAD_GLOBAL 8 (Exception)
780 CHECK_EXC_MATCH
782 POP_JUMP_FORWARD_IF_FALSE 3 (to 790)
784 POP_TOP

786 POP_EXCEPT
788 RETURN_VALUE

790 RERAISE 0
792 COPY 3
794 POP_EXCEPT
796 RERAISE 1

798 LOAD_GLOBAL 27 (NULL + log_automation_step)
800 LOAD_DEREF 0 (self)
802 LOAD_ATTR 6 (logger)
804 LOAD_CONST 30 ("GCP_PROJECT")
806 LOAD_CONST 31 ("PARSED")
808 LOAD_CONST 32 ("project_id")
810 LOAD_FAST 8 (project_id)
812 BUILD_MAP 1
814 CALL 4
816 POP_TOP

818 LOAD_GLOBAL 43 (NULL + enable_key_action)
820 LOAD_FAST 5 (inc_page)
822 LOAD_DEREF 0 (self)
824 LOAD_ATTR 6 (logger)
826 LOAD_FAST 8 (project_id)
828 LOAD_CONST 33 (180)
830 KW_NAMES 12 (('timeout_sec',))
832 CALL 4
834 GET_AWAITABLE 0
836 LOAD_CONST 3 (None)
838 SEND 3 (to 844)
840 YIELD_VALUE
842 JUMP_BACKWARD_NO_INTERRUPT 4 (to 838)
844 STORE_FAST 10 (api_res)

846 LOAD_FAST 10 (api_res)
848 LOAD_METHOD 7 (get)
850 LOAD_CONST 34 ("api_key")
852 LOAD_CONST 18 ("")
854 CALL 2
856 STORE_FAST 11 (api_key_val)

858 LOAD_FAST 10 (api_res)
860 LOAD_METHOD 7 (get)
862 LOAD_CONST 7 ("success")
864 CALL 1
866 POP_JUMP_FORWARD_IF_FALSE 2 (to 872)
868 LOAD_FAST 11 (api_key_val)
870 POP_JUMP_FORWARD_IF_TRUE 156 (to 1020)

872 LOAD_GLOBAL 27 (NULL + log_automation_step)
874 LOAD_DEREF 0 (self)
876 LOAD_ATTR 6 (logger)
878 LOAD_CONST 35 ("API_KEY")
880 LOAD_CONST 36 ("FAILED_CREATE_OR_EXTRACT")
882 CALL 3
884 POP_TOP

886 LOAD_CONST 8 (False)

888 LOAD_CONST 37 ("Failed to create or extract API key")
890 LOAD_FAST 8 (project_id)

892 LOAD_GLOBAL 41 (NULL + hasattr)
894 LOAD_FAST 5 (inc_page)
896 LOAD_CONST 17 ("url")
898 CALL 2
900 POP_JUMP_FORWARD_IF_FALSE 7 (to 908)
902 LOAD_FAST 5 (inc_page)
904 LOAD_ATTR 18 (url)
906 JUMP_FORWARD 1 (to 910)

908 LOAD_CONST 18 ("")
910 LOAD_CONST 5 (True)

912 LOAD_CONST 38 (('success', 'error', 'project_id', 'console_url', 'console_opened'))
914 BUILD_CONST_KEY_MAP 5

916 NOP

918 LOAD_FAST 4 (inc_ctx)
920 POP_JUMP_FORWARD_IF_FALSE 33 (to 946)
922 LOAD_DEREF 0 (self)
924 LOAD_ATTR 10 (keep_browser_open)
926 POP_JUMP_FORWARD_IF_TRUE 26 (to 946)

928 LOAD_FAST 4 (inc_ctx)
930 LOAD_METHOD 11 (close)
932 CALL 0
934 GET_AWAITABLE 0
936 LOAD_CONST 3 (None)
938 SEND 3 (to 944)
940 YIELD_VALUE
942 JUMP_BACKWARD_NO_INTERRUPT 4 (to 938)
944 POP_TOP
946 JUMP_FORWARD 16 (to 970)
948 PUSH_EXC_INFO

950 LOAD_GLOBAL 8 (Exception)
952 CHECK_EXC_MATCH
954 POP_JUMP_FORWARD_IF_FALSE 3 (to 962)
956 POP_TOP

958 POP_EXCEPT
960 JUMP_FORWARD 4 (to 970)

962 RERAISE 0
964 COPY 3
966 POP_EXCEPT
968 RERAISE 1

970 LOAD_FAST 2 (prev_mode)
972 LOAD_DEREF 0 (self)
974 STORE_ATTR 2 (_popup_mode)

976 NOP

978 LOAD_DEREF 0 (self)
980 LOAD_METHOD 8 (_bind_single_page_policy)
982 CALL 0
984 GET_AWAITABLE 0
986 LOAD_CONST 3 (None)
988 SEND 3 (to 994)
990 YIELD_VALUE
992 JUMP_BACKWARD_NO_INTERRUPT 4 (to 988)
994 POP_TOP
996 RETURN_VALUE
998 PUSH_EXC_INFO

1000 LOAD_GLOBAL 8 (Exception)
1002 CHECK_EXC_MATCH
1004 POP_JUMP_FORWARD_IF_FALSE 3 (to 1012)
1006 POP_TOP

1008 POP_EXCEPT
1010 RETURN_VALUE

1012 RERAISE 0
1014 COPY 3
1016 POP_EXCEPT
1018 RERAISE 1

1020 LOAD_GLOBAL 27 (NULL + log_automation_step)
1022 LOAD_DEREF 0 (self)
1024 LOAD_ATTR 6 (logger)
1026 LOAD_CONST 35 ("API_KEY")
1028 LOAD_CONST 39 ("SUCCESS")
1030 LOAD_CONST 40 ("prefix")
1032 LOAD_FAST 11 (api_key_val)
1034 LOAD_CONST 3 (None)
1036 LOAD_CONST 41 (10)
1038 BUILD_SLICE 2
1040 BINARY_SUBSCR
1042 BUILD_MAP 1
1044 CALL 4
1046 POP_TOP

1048 LOAD_CONST 5 (True)

1050 LOAD_GLOBAL 29 (NULL + getattr)
1052 LOAD_DEREF 0 (self)
1054 LOAD_ATTR 0 (page)
1056 LOAD_CONST 17 ("url")
1058 LOAD_CONST 18 ("")
1060 CALL 3

1062 LOAD_CONST 5 (True)

1064 LOAD_GLOBAL 41 (NULL + hasattr)
1066 LOAD_FAST 5 (inc_page)
1068 LOAD_CONST 17 ("url")
1070 CALL 2
1072 POP_JUMP_FORWARD_IF_FALSE 7 (to 1080)
1074 LOAD_FAST 5 (inc_page)
1076 LOAD_ATTR 18 (url)
1078 JUMP_FORWARD 1 (to 1082)

1080 LOAD_CONST 18 ("")
1082 LOAD_CONST 5 (True)

1084 LOAD_FAST 8 (project_id)

1086 LOAD_FAST 11 (api_key_val)

1088 LOAD_CONST 42 (('success', 'url', 'console_opened', 'console_url', 'console_incognito', 'project_id', 'api_key'))
1090 BUILD_CONST_KEY_MAP 7
1092 STORE_FAST 12 (result_out)

1094 NOP

1096 LOAD_FAST 4 (inc_ctx)
1098 POP_JUMP_FORWARD_IF_FALSE 26 (to 1118)

1100 LOAD_FAST 4 (inc_ctx)
1102 LOAD_METHOD 11 (close)
1104 CALL 0
1106 GET_AWAITABLE 0
1108 LOAD_CONST 3 (None)
1110 SEND 3 (to 1116)
1112 YIELD_VALUE
1114 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1110)
1116 POP_TOP
1118 JUMP_FORWARD 16 (to 1142)
1120 PUSH_EXC_INFO

1122 LOAD_GLOBAL 8 (Exception)
1124 CHECK_EXC_MATCH
1126 POP_JUMP_FORWARD_IF_FALSE 3 (to 1134)
1128 POP_TOP

1130 POP_EXCEPT
1132 JUMP_FORWARD 4 (to 1142)

1134 RERAISE 0
1136 COPY 3
1138 POP_EXCEPT
1140 RERAISE 1

1142 NOP

1144 LOAD_DEREF 0 (self)
1146 LOAD_METHOD 22 (_cleanup)
1148 CALL 0
1150 GET_AWAITABLE 0
1152 LOAD_CONST 3 (None)
1154 SEND 3 (to 1160)
1156 YIELD_VALUE
1158 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1154)
1160 POP_TOP
1162 JUMP_FORWARD 16 (to 1186)
1164 PUSH_EXC_INFO

1166 LOAD_GLOBAL 8 (Exception)
1168 CHECK_EXC_MATCH
1170 POP_JUMP_FORWARD_IF_FALSE 3 (to 1178)
1172 POP_TOP

1174 POP_EXCEPT
1176 JUMP_FORWARD 4 (to 1186)

1178 RERAISE 0
1180 COPY 3
1182 POP_EXCEPT
1184 RERAISE 1

1186 LOAD_FAST 12 (result_out)

1188 NOP

1190 LOAD_FAST 4 (inc_ctx)
1192 POP_JUMP_FORWARD_IF_FALSE 33 (to 1218)
1194 LOAD_DEREF 0 (self)
1196 LOAD_ATTR 10 (keep_browser_open)
1198 POP_JUMP_FORWARD_IF_TRUE 26 (to 1218)

1200 LOAD_FAST 4 (inc_ctx)
1202 LOAD_METHOD 11 (close)
1204 CALL 0
1206 GET_AWAITABLE 0
1208 LOAD_CONST 3 (None)
1210 SEND 3 (to 1216)
1212 YIELD_VALUE
1214 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1210)
1216 POP_TOP
1218 JUMP_FORWARD 16 (to 1242)
1220 PUSH_EXC_INFO

1222 LOAD_GLOBAL 8 (Exception)
1224 CHECK_EXC_MATCH
1226 POP_JUMP_FORWARD_IF_FALSE 3 (to 1234)
1228 POP_TOP

1230 POP_EXCEPT
1232 JUMP_FORWARD 4 (to 1242)

1234 RERAISE 0
1236 COPY 3
1238 POP_EXCEPT
1240 RERAISE 1

1242 LOAD_FAST 2 (prev_mode)
1244 LOAD_DEREF 0 (self)
1246 STORE_ATTR 2 (_popup_mode)

1248 NOP

1250 LOAD_DEREF 0 (self)
1252 LOAD_METHOD 8 (_bind_single_page_policy)
1254 CALL 0
1256 GET_AWAITABLE 0
1258 LOAD_CONST 3 (None)
1260 SEND 3 (to 1266)
1262 YIELD_VALUE
1264 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1260)
1266 POP_TOP
1268 RETURN_VALUE
1270 PUSH_EXC_INFO

1272 LOAD_GLOBAL 8 (Exception)
1274 CHECK_EXC_MATCH
1276 POP_JUMP_FORWARD_IF_FALSE 3 (to 1284)
1278 POP_TOP

1280 POP_EXCEPT
1282 RETURN_VALUE

1284 RERAISE 0
1286 COPY 3
1288 POP_EXCEPT
1290 RERAISE 1
1292 PUSH_EXC_INFO

1294 NOP

1296 LOAD_FAST 4 (inc_ctx)
1298 POP_JUMP_FORWARD_IF_FALSE 34 (to 1326)
1300 LOAD_DEREF 0 (self)
1302 LOAD_ATTR 10 (keep_browser_open)
1304 POP_JUMP_FORWARD_IF_TRUE 28 (to 1328)

1306 LOAD_FAST 4 (inc_ctx)
1308 LOAD_METHOD 11 (close)
1310 CALL 0
1312 GET_AWAITABLE 0
1314 LOAD_CONST 3 (None)
1316 SEND 3 (to 1322)
1318 YIELD_VALUE
1320 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1316)
1322 POP_TOP
1324 RERAISE 0

1326 RERAISE 0
1328 RERAISE 0
1330 PUSH_EXC_INFO

1332 LOAD_GLOBAL 8 (Exception)
1334 CHECK_EXC_MATCH
1336 POP_JUMP_FORWARD_IF_FALSE 3 (to 1344)
1338 POP_TOP

1340 POP_EXCEPT
1342 RERAISE 0

1344 RERAISE 0
1346 COPY 3
1348 POP_EXCEPT
1350 RERAISE 1
1352 COPY 3
1354 POP_EXCEPT
1356 RERAISE 1
1358 PUSH_EXC_INFO

1360 LOAD_GLOBAL 8 (Exception)
1362 CHECK_EXC_MATCH
1364 POP_JUMP_FORWARD_IF_FALSE 116 (to 1472)
1366 STORE_FAST 13 (e)

1368 LOAD_GLOBAL 27 (NULL + log_automation_step)
1370 LOAD_DEREF 0 (self)
1372 LOAD_ATTR 6 (logger)
1374 LOAD_CONST 43 ("LAB_START")
1376 LOAD_CONST 44 ("ERROR")
1378 LOAD_CONST 45 ("error")
1380 LOAD_GLOBAL 47 (NULL + str)
1382 LOAD_FAST 13 (e)
1384 CALL 1
1386 BUILD_MAP 1
1388 CALL 4
1390 POP_TOP

1392 LOAD_CONST 8 (False)
1394 LOAD_GLOBAL 47 (NULL + str)
1396 LOAD_FAST 13 (e)
1398 CALL 1
1400 LOAD_CONST 10 (('success', 'error'))
1402 BUILD_CONST_KEY_MAP 2
1404 SWAP 2
1406 POP_EXCEPT
1408 LOAD_CONST 3 (None)
1410 STORE_FAST 13 (e)
1412 DELETE_FAST 13 (e)

1414 LOAD_FAST 2 (prev_mode)
1416 LOAD_DEREF 0 (self)
1418 STORE_ATTR 2 (_popup_mode)

1420 NOP

1422 LOAD_DEREF 0 (self)
1424 LOAD_METHOD 8 (_bind_single_page_policy)
1426 CALL 0
1428 GET_AWAITABLE 0
1430 LOAD_CONST 3 (None)
1432 SEND 3 (to 1438)
1434 YIELD_VALUE
1436 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1432)
1438 POP_TOP
1440 RETURN_VALUE
1442 PUSH_EXC_INFO

1444 LOAD_GLOBAL 8 (Exception)
1446 CHECK_EXC_MATCH
1448 POP_JUMP_FORWARD_IF_FALSE 3 (to 1456)
1450 POP_TOP

1452 POP_EXCEPT
1454 RETURN_VALUE

1456 RERAISE 0
1458 COPY 3
1460 POP_EXCEPT
1462 RERAISE 1
1464 LOAD_CONST 3 (None)
1466 STORE_FAST 13 (e)
1468 DELETE_FAST 13 (e)
1470 RERAISE 1

1472 RERAISE 0
1474 COPY 3
1476 POP_EXCEPT
1478 RERAISE 1
1480 PUSH_EXC_INFO

1482 LOAD_FAST 2 (prev_mode)
1484 LOAD_DEREF 0 (self)
1486 STORE_ATTR 2 (_popup_mode)

1488 NOP

1490 LOAD_DEREF 0 (self)
1492 LOAD_METHOD 8 (_bind_single_page_policy)
1494 CALL 0
1496 GET_AWAITABLE 0
1498 LOAD_CONST 3 (None)
1500 SEND 3 (to 1506)
1502 YIELD_VALUE
1504 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1500)
1506 POP_TOP
1508 RERAISE 0
1510 PUSH_EXC_INFO

1512 LOAD_GLOBAL 8 (Exception)
1514 CHECK_EXC_MATCH
1516 POP_JUMP_FORWARD_IF_FALSE 3 (to 1524)
1518 POP_TOP

1520 POP_EXCEPT
1522 RERAISE 0

1524 RERAISE 0
1526 COPY 3
1528 POP_EXCEPT
1530 RERAISE 1
1532 COPY 3
1534 POP_EXCEPT
1536 RERAISE 1

0 COPY_FREE_VARS 1

2 LOAD_DEREF 0 (self)
4 LOAD_METHOD 0 (_handle_captcha)
6 CALL 0
8 RETURN_VALUE


0 NOP

2 LOAD_FAST 0 (self)
4 LOAD_METHOD 0 (_run_async)
6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_cleanup)
10 CALL 0
12 CALL 1
14 POP_TOP
16 LOAD_CONST 1 (None)
18 RETURN_VALUE
20 PUSH_EXC_INFO

22 LOAD_GLOBAL 4 (Exception)
24 CHECK_EXC_MATCH
26 POP_JUMP_FORWARD_IF_FALSE 4 (to 36)
28 POP_TOP

30 POP_EXCEPT
32 LOAD_CONST 1 (None)
34 RETURN_VALUE

36 RERAISE 0
38 COPY 3
40 POP_EXCEPT
42 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("EMAIL_CONFIRM")
12 LOAD_CONST 2 ("START")
14 LOAD_CONST 3 ("url")
16 LOAD_FAST 1 (url)
18 BUILD_MAP 1
20 CALL 4
22 POP_TOP

24 NOP

26 LOAD_FAST 0 (self)
28 LOAD_METHOD 2 (_ensure_page_ready)
30 CALL 0
32 GET_AWAITABLE 0
34 LOAD_CONST 4 (None)
36 SEND 3 (to 42)
38 YIELD_VALUE
40 JUMP_BACKWARD_NO_INTERRUPT 4 (to 36)
42 POP_TOP

44 LOAD_FAST 0 (self)
46 LOAD_ATTR 3 (context)
48 POP_JUMP_FORWARD_IF_FALSE 7 (to 56)
50 LOAD_FAST 0 (self)
52 LOAD_ATTR 4 (page)
54 POP_JUMP_FORWARD_IF_TRUE 15 (to 64)

56 LOAD_GLOBAL 11 (NULL + RuntimeError)
58 LOAD_CONST 5 ("Context/Page not initialized")
60 CALL 1
62 RAISE_VARARGS 1 (exception instance)

64 LOAD_GLOBAL 13 (NULL + confirm_via_link_action)

66 LOAD_FAST 0 (self)
68 LOAD_ATTR 3 (context)

70 LOAD_FAST 0 (self)
72 LOAD_ATTR 4 (page)

74 LOAD_FAST 0 (self)
76 LOAD_ATTR 1 (logger)

78 LOAD_FAST 1 (url)

80 LOAD_FAST 2 (password)

82 LOAD_FAST 3 (email)

84 CALL 6
86 GET_AWAITABLE 0
88 LOAD_CONST 4 (None)
90 SEND 3 (to 96)
92 YIELD_VALUE
94 JUMP_BACKWARD_NO_INTERRUPT 4 (to 90)
96 STORE_FAST 4 (result)

98 NOP

100 LOAD_FAST 0 (self)
102 LOAD_ATTR 3 (context)
104 LOAD_ATTR 7 (pages)
106 POP_JUMP_FORWARD_IF_FALSE 23 (to 122)

108 LOAD_FAST 0 (self)
110 LOAD_ATTR 3 (context)
112 LOAD_ATTR 7 (pages)
114 LOAD_CONST 6 (-1)
116 BINARY_SUBSCR
118 LOAD_FAST 0 (self)
120 STORE_ATTR 4 (page)
122 JUMP_FORWARD 16 (to 146)
124 PUSH_EXC_INFO

126 LOAD_GLOBAL 16 (Exception)
128 CHECK_EXC_MATCH
130 POP_JUMP_FORWARD_IF_FALSE 3 (to 138)
132 POP_TOP

134 POP_EXCEPT
136 JUMP_FORWARD 4 (to 146)

138 RERAISE 0
140 COPY 3
142 POP_EXCEPT
144 RERAISE 1

146 LOAD_FAST 4 (result)
148 RETURN_VALUE
150 PUSH_EXC_INFO

152 LOAD_GLOBAL 16 (Exception)
154 CHECK_EXC_MATCH
156 POP_JUMP_FORWARD_IF_FALSE 66 (to 216)
158 STORE_FAST 5 (e)

160 LOAD_GLOBAL 1 (NULL + log_automation_step)
162 LOAD_FAST 0 (self)
164 LOAD_ATTR 1 (logger)
166 LOAD_CONST 1 ("EMAIL_CONFIRM")
168 LOAD_CONST 7 ("ERROR")
170 LOAD_CONST 8 ("error")
172 LOAD_GLOBAL 19 (NULL + str)
174 LOAD_FAST 5 (e)
176 CALL 1
178 BUILD_MAP 1
180 CALL 4
182 POP_TOP

184 LOAD_CONST 9 (False)
186 LOAD_GLOBAL 19 (NULL + str)
188 LOAD_FAST 5 (e)
190 CALL 1
192 LOAD_CONST 10 (('success', 'error'))
194 BUILD_CONST_KEY_MAP 2
196 SWAP 2
198 POP_EXCEPT
200 LOAD_CONST 4 (None)
202 STORE_FAST 5 (e)
204 DELETE_FAST 5 (e)
206 RETURN_VALUE
208 LOAD_CONST 4 (None)
210 STORE_FAST 5 (e)
212 DELETE_FAST 5 (e)
214 RERAISE 1

216 RERAISE 0
218 COPY 3
220 POP_EXCEPT
222 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_CONST 1 (False)
8 STORE_FAST 1 (needs_init)

10 LOAD_FAST 0 (self)
12 LOAD_ATTR 0 (context)
14 POP_JUMP_FORWARD_IF_FALSE 7 (to 22)
16 LOAD_FAST 0 (self)
18 LOAD_ATTR 1 (page)
20 POP_JUMP_FORWARD_IF_TRUE 3 (to 28)

22 LOAD_CONST 2 (True)
24 STORE_FAST 1 (needs_init)
26 JUMP_FORWARD 47 (to 72)

28 NOP

30 LOAD_FAST 0 (self)
32 LOAD_ATTR 1 (page)
34 LOAD_METHOD 2 (is_closed)
36 CALL 0
38 POP_JUMP_FORWARD_IF_FALSE 2 (to 44)

40 LOAD_CONST 2 (True)
42 STORE_FAST 1 (needs_init)
44 JUMP_FORWARD 18 (to 72)
46 PUSH_EXC_INFO

48 LOAD_GLOBAL 6 (Exception)
50 CHECK_EXC_MATCH
52 POP_JUMP_FORWARD_IF_FALSE 5 (to 64)
54 POP_TOP

56 LOAD_CONST 2 (True)
58 STORE_FAST 1 (needs_init)
60 POP_EXCEPT
62 JUMP_FORWARD 4 (to 72)

64 RERAISE 0
66 COPY 3
68 POP_EXCEPT
70 RERAISE 1

72 LOAD_FAST 1 (needs_init)
74 POP_JUMP_FORWARD_IF_FALSE 28 (to 98)

76 LOAD_FAST 0 (self)
78 LOAD_METHOD 4 (_init_browser)
80 CALL 0
82 GET_AWAITABLE 0
84 LOAD_CONST 3 (None)
86 SEND 3 (to 92)
88 YIELD_VALUE
90 JUMP_BACKWARD_NO_INTERRUPT 4 (to 86)
92 POP_TOP
94 LOAD_CONST 3 (None)
96 RETURN_VALUE

98 LOAD_CONST 3 (None)
100 RETURN_VALUE
102 PUSH_EXC_INFO

104 LOAD_GLOBAL 6 (Exception)
106 CHECK_EXC_MATCH
108 POP_JUMP_FORWARD_IF_FALSE 30 (to 136)
110 POP_TOP

112 LOAD_FAST 0 (self)
114 LOAD_METHOD 4 (_init_browser)
116 CALL 0
118 GET_AWAITABLE 0
120 LOAD_CONST 3 (None)
122 SEND 3 (to 128)
124 YIELD_VALUE
126 JUMP_BACKWARD_NO_INTERRUPT 4 (to 122)
128 POP_TOP
130 POP_EXCEPT
132 LOAD_CONST 3 (None)
134 RETURN_VALUE

136 RERAISE 0
138 COPY 3
140 POP_EXCEPT
142 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_FAST 0 (self)
8 LOAD_ATTR 0 (context)
10 POP_JUMP_FORWARD_IF_TRUE 2 (to 16)

12 LOAD_CONST 1 (None)
14 RETURN_VALUE

16 LOAD_GLOBAL 3 (NULL + list)
18 LOAD_FAST 0 (self)
20 LOAD_ATTR 0 (context)
22 LOAD_ATTR 2 (pages)
24 CALL 1
26 GET_ITER
28 FOR_ITER 139 (to 162)
30 STORE_FAST 2 (p)

32 NOP

34 LOAD_FAST 1 (keep_current)
36 POP_JUMP_FORWARD_IF_FALSE 19 (to 56)
38 LOAD_FAST 0 (self)
40 LOAD_ATTR 3 (page)
42 POP_JUMP_FORWARD_IF_FALSE 12 (to 56)
44 LOAD_FAST 2 (p)
46 LOAD_FAST 0 (self)
48 LOAD_ATTR 3 (page)
50 COMPARE_OP 2 (==)
52 POP_JUMP_FORWARD_IF_FALSE 1 (to 56)

54 JUMP_BACKWARD 24 (to 28)

56 LOAD_CONST 2 ("")
58 STORE_FAST 3 (url)

60 NOP

62 LOAD_FAST 2 (p)
64 LOAD_ATTR 4 (url)
66 STORE_FAST 3 (url)
68 JUMP_FORWARD 18 (to 96)
70 PUSH_EXC_INFO

72 LOAD_GLOBAL 10 (Exception)
74 CHECK_EXC_MATCH
76 POP_JUMP_FORWARD_IF_FALSE 5 (to 88)
78 POP_TOP

80 LOAD_CONST 2 ("")
82 STORE_FAST 3 (url)
84 POP_EXCEPT
86 JUMP_FORWARD 4 (to 96)

88 RERAISE 0
90 COPY 3
92 POP_EXCEPT
94 RERAISE 1

96 LOAD_FAST 2 (p)
98 LOAD_METHOD 6 (is_closed)
100 CALL 0
102 POP_JUMP_FORWARD_IF_TRUE 50 (to 138)

104 LOAD_FAST 3 (url)
106 JUMP_IF_TRUE_OR_POP 1 (to 110)
108 LOAD_CONST 2 ("")
110 LOAD_METHOD 7 (startswith)
112 LOAD_CONST 3 ("about:blank")
114 CALL 1
116 POP_JUMP_FORWARD_IF_TRUE 1 (to 120)
118 NOP

120 LOAD_FAST 2 (p)
122 LOAD_METHOD 8 (close)
124 CALL 0
126 GET_AWAITABLE 0
128 LOAD_CONST 1 (None)
130 SEND 3 (to 136)
132 YIELD_VALUE
134 JUMP_BACKWARD_NO_INTERRUPT 4 (to 130)
136 POP_TOP
138 JUMP_BACKWARD 124 (to 28)
140 PUSH_EXC_INFO

142 LOAD_GLOBAL 10 (Exception)
144 CHECK_EXC_MATCH
146 POP_JUMP_FORWARD_IF_FALSE 3 (to 154)
148 POP_TOP

150 POP_EXCEPT
152 JUMP_BACKWARD 136 (to 28)

154 RERAISE 0
156 COPY 3
158 POP_EXCEPT
160 RERAISE 1

162 LOAD_CONST 1 (None)
164 RETURN_VALUE
166 PUSH_EXC_INFO

168 LOAD_GLOBAL 10 (Exception)
170 CHECK_EXC_MATCH
172 POP_JUMP_FORWARD_IF_FALSE 4 (to 182)
174 POP_TOP

176 POP_EXCEPT
178 LOAD_CONST 1 (None)
180 RETURN_VALUE

182 RERAISE 0
184 COPY 3
186 POP_EXCEPT
188 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("BROWSER_INIT")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_GLOBAL 5 (NULL + _ensure_playwright_browsers_path)
22 CALL 0
24 POP_TOP
26 JUMP_FORWARD 16 (to 50)
28 PUSH_EXC_INFO

30 LOAD_GLOBAL 6 (Exception)
32 CHECK_EXC_MATCH
34 POP_JUMP_FORWARD_IF_FALSE 3 (to 42)
36 POP_TOP

38 POP_EXCEPT
40 JUMP_FORWARD 4 (to 50)

42 RERAISE 0
44 COPY 3
46 POP_EXCEPT
48 RERAISE 1

50 LOAD_GLOBAL 9 (NULL + async_playwright)
52 CALL 0
54 LOAD_METHOD 5 (start)
56 CALL 0
58 GET_AWAITABLE 0
60 LOAD_CONST 3 (None)
62 SEND 3 (to 68)
64 YIELD_VALUE
66 JUMP_BACKWARD_NO_INTERRUPT 4 (to 62)
68 STORE_FAST 1 (pw)

70 LOAD_GLOBAL 13 (NULL + _get_bundle_root)
72 CALL 0
74 STORE_FAST 2 (project_root)

76 LOAD_FAST 0 (self)
78 LOAD_METHOD 7 (get_default_pw_state_path)
80 CALL 0
82 STORE_FAST 3 (state_path_str)

84 LOAD_FAST 0 (self)
86 LOAD_METHOD 8 (get_default_pw_profile_dir)
88 CALL 0
90 STORE_FAST 4 (user_data_dir_str)

92 NOP

94 LOAD_GLOBAL 19 (NULL + os)
96 LOAD_ATTR 10 (makedirs)
98 LOAD_GLOBAL 18 (os)
100 LOAD_ATTR 11 (path)
102 LOAD_METHOD 12 (dirname)
104 LOAD_FAST 3 (state_path_str)
106 CALL 1
108 LOAD_CONST 4 (True)
110 KW_NAMES 5 (('exist_ok',))
112 CALL 2
114 POP_TOP

116 LOAD_GLOBAL 19 (NULL + os)
118 LOAD_ATTR 10 (makedirs)
120 LOAD_FAST 4 (user_data_dir_str)
122 LOAD_CONST 4 (True)
124 KW_NAMES 5 (('exist_ok',))
126 CALL 2
128 POP_TOP
130 JUMP_FORWARD 16 (to 154)
132 PUSH_EXC_INFO

134 LOAD_GLOBAL 6 (Exception)
136 CHECK_EXC_MATCH
138 POP_JUMP_FORWARD_IF_FALSE 3 (to 146)
140 POP_TOP

142 POP_EXCEPT
144 JUMP_FORWARD 4 (to 154)

146 RERAISE 0
148 COPY 3
150 POP_EXCEPT
152 RERAISE 1

154 LOAD_FAST 2 (project_root)
156 LOAD_CONST 6 ("AntiCaptcha")
158 BINARY_OP 11
160 STORE_FAST 5 (ext_dir)

162 NOP

164 LOAD_GLOBAL 27 (NULL + Path)
166 LOAD_FAST 3 (state_path_str)
168 CALL 1
170 STORE_FAST 6 (sp)

172 LOAD_FAST 6 (sp)
174 LOAD_METHOD 14 (exists)
176 CALL 0
178 POP_JUMP_FORWARD_IF_FALSE 20 (to 188)

180 LOAD_FAST 6 (sp)
182 LOAD_METHOD 15 (unlink)
184 CALL 0
186 POP_TOP
188 JUMP_FORWARD 16 (to 212)
190 PUSH_EXC_INFO

192 LOAD_GLOBAL 6 (Exception)
194 CHECK_EXC_MATCH
196 POP_JUMP_FORWARD_IF_FALSE 3 (to 204)
198 POP_TOP

200 POP_EXCEPT
202 JUMP_FORWARD 4 (to 212)

204 RERAISE 0
206 COPY 3
208 POP_EXCEPT
210 RERAISE 1

212 NOP

214 LOAD_CONST 7 (0)
216 LOAD_CONST 3 (None)
218 IMPORT_NAME 16 (shutil)
220 STORE_FAST 7 (shutil)

222 LOAD_GLOBAL 18 (os)
224 LOAD_ATTR 11 (path)
226 LOAD_METHOD 17 (isdir)
228 LOAD_FAST 4 (user_data_dir_str)
230 CALL 1
232 POP_JUMP_FORWARD_IF_FALSE 23 (to 248)

234 LOAD_FAST 7 (shutil)
236 LOAD_METHOD 18 (rmtree)
238 LOAD_FAST 4 (user_data_dir_str)
240 LOAD_CONST 4 (True)
242 KW_NAMES 8 (('ignore_errors',))
244 CALL 2
246 POP_TOP
248 JUMP_FORWARD 16 (to 272)
250 PUSH_EXC_INFO

252 LOAD_GLOBAL 6 (Exception)
254 CHECK_EXC_MATCH
256 POP_JUMP_FORWARD_IF_FALSE 3 (to 264)
258 POP_TOP

260 POP_EXCEPT
262 JUMP_FORWARD 4 (to 272)

264 RERAISE 0
266 COPY 3
268 POP_EXCEPT
270 RERAISE 1

272 LOAD_FAST 0 (self)
274 LOAD_ATTR 19 (extension_mode)
276 POP_JUMP_FORWARD_IF_FALSE 342 (to 540)
278 LOAD_FAST 5 (ext_dir)
280 LOAD_METHOD 14 (exists)
282 CALL 0
284 POP_JUMP_FORWARD_IF_FALSE 321 (to 540)

286 NOP

288 LOAD_CONST 9 ("--disable-blink-features=AutomationControlled")
290 LOAD_CONST 10 ("--disable-extensions-except=")
292 LOAD_FAST 5 (ext_dir)
294 FORMAT_VALUE 0
296 BUILD_STRING 2

298 LOAD_CONST 11 ("--load-extension=")
300 LOAD_FAST 5 (ext_dir)
302 FORMAT_VALUE 0
304 BUILD_STRING 2

306 BUILD_LIST 3
308 STORE_FAST 8 (args)

310 LOAD_FAST 1 (pw)
312 LOAD_ATTR 20 (chromium)
314 LOAD_METHOD 21 (launch_persistent_context)

316 LOAD_GLOBAL 45 (NULL + str)
318 LOAD_FAST 4 (user_data_dir_str)
320 CALL 1

322 LOAD_CONST 12 (False)

324 LOAD_FAST 8 (args)

326 LOAD_CONST 3 (None)

328 LOAD_GLOBAL 46 (settings)
330 LOAD_ATTR 24 (BROWSER_USER_AGENT)

332 LOAD_CONST 13 ("en-US")
334 KW_NAMES 14 (('user_data_dir', 'headless', 'args', 'viewport', 'user_agent', 'locale'))
336 CALL 6
338 GET_AWAITABLE 0
340 LOAD_CONST 3 (None)
342 SEND 3 (to 348)
344 YIELD_VALUE
346 JUMP_BACKWARD_NO_INTERRUPT 4 (to 342)
348 LOAD_FAST 0 (self)
350 STORE_ATTR 25 (context)

352 NOP

354 LOAD_FAST 0 (self)
356 LOAD_ATTR 25 (context)
358 LOAD_ATTR 26 (browser)
360 LOAD_FAST 0 (self)
362 STORE_ATTR 26 (browser)
364 JUMP_FORWARD 23 (to 394)
366 PUSH_EXC_INFO

368 LOAD_GLOBAL 6 (Exception)
370 CHECK_EXC_MATCH
372 POP_JUMP_FORWARD_IF_FALSE 10 (to 386)
374 POP_TOP

376 LOAD_CONST 3 (None)
378 LOAD_FAST 0 (self)
380 STORE_ATTR 26 (browser)
382 POP_EXCEPT
384 JUMP_FORWARD 4 (to 394)

386 RERAISE 0
388 COPY 3
390 POP_EXCEPT
392 RERAISE 1

394 LOAD_FAST 0 (self)
396 LOAD_METHOD 27 (_bind_single_page_policy)
398 CALL 0
400 GET_AWAITABLE 0
402 LOAD_CONST 3 (None)
404 SEND 3 (to 410)
406 YIELD_VALUE
408 JUMP_BACKWARD_NO_INTERRUPT 4 (to 404)
410 POP_TOP

412 LOAD_FAST 0 (self)
414 LOAD_ATTR 25 (context)
416 LOAD_METHOD 28 (new_page)
418 CALL 0
420 GET_AWAITABLE 0
422 LOAD_CONST 3 (None)
424 SEND 3 (to 430)
426 YIELD_VALUE
428 JUMP_BACKWARD_NO_INTERRUPT 4 (to 424)
430 LOAD_FAST 0 (self)
432 STORE_ATTR 29 (page)

434 LOAD_FAST 0 (self)
436 LOAD_ATTR 29 (page)
438 LOAD_METHOD 30 (set_default_timeout)
440 LOAD_GLOBAL 46 (settings)
442 LOAD_ATTR 31 (PLAYWRIGHT_TIMEOUT)
444 CALL 1
446 POP_TOP

448 LOAD_GLOBAL 1 (NULL + log_automation_step)
450 LOAD_FAST 0 (self)
452 LOAD_ATTR 1 (logger)
454 LOAD_CONST 1 ("BROWSER_INIT")
456 LOAD_CONST 15 ("EXTENSION_MODE")
458 LOAD_GLOBAL 45 (NULL + str)
460 LOAD_FAST 5 (ext_dir)
462 CALL 1
464 LOAD_FAST 4 (user_data_dir_str)
466 LOAD_CONST 16 (('ext_dir', 'profile'))
468 BUILD_CONST_KEY_MAP 2
470 CALL 4
472 POP_TOP

474 LOAD_CONST 3 (None)
476 RETURN_VALUE
478 PUSH_EXC_INFO

480 LOAD_GLOBAL 6 (Exception)
482 CHECK_EXC_MATCH
484 POP_JUMP_FORWARD_IF_FALSE 49 (to 532)
486 STORE_FAST 9 (e)

488 LOAD_GLOBAL 1 (NULL + log_automation_step)
490 LOAD_FAST 0 (self)
492 LOAD_ATTR 1 (logger)
494 LOAD_CONST 1 ("BROWSER_INIT")
496 LOAD_CONST 17 ("EXTENSION_MODE_FAILED")
498 LOAD_GLOBAL 45 (NULL + str)
500 LOAD_FAST 9 (e)
502 CALL 1
504 LOAD_FAST 4 (user_data_dir_str)
506 LOAD_CONST 18 (('error', 'profile'))
508 BUILD_CONST_KEY_MAP 2
510 CALL 4
512 POP_TOP
514 POP_EXCEPT
516 LOAD_CONST 3 (None)
518 STORE_FAST 9 (e)
520 DELETE_FAST 9 (e)
522 JUMP_FORWARD 8 (to 540)
524 LOAD_CONST 3 (None)
526 STORE_FAST 9 (e)
528 DELETE_FAST 9 (e)
530 RERAISE 1

532 RERAISE 0
534 COPY 3
536 POP_EXCEPT
538 RERAISE 1

540 LOAD_FAST 1 (pw)
542 LOAD_ATTR 20 (chromium)
544 LOAD_METHOD 32 (launch)

546 LOAD_FAST 0 (self)
548 LOAD_ATTR 33 (headless)

550 LOAD_CONST 9 ("--disable-blink-features=AutomationControlled")
552 BUILD_LIST 1

554 KW_NAMES 19 (('headless', 'args'))
556 CALL 2
558 GET_AWAITABLE 0
560 LOAD_CONST 3 (None)
562 SEND 3 (to 568)
564 YIELD_VALUE
566 JUMP_BACKWARD_NO_INTERRUPT 4 (to 562)
568 LOAD_FAST 0 (self)
570 STORE_ATTR 26 (browser)

572 LOAD_CONST 3 (None)

574 LOAD_GLOBAL 46 (settings)
576 LOAD_ATTR 24 (BROWSER_USER_AGENT)

578 LOAD_CONST 13 ("en-US")
580 LOAD_CONST 20 (('viewport', 'user_agent', 'locale'))
582 BUILD_CONST_KEY_MAP 3
584 STORE_FAST 10 (context_kwargs)

586 PUSH_NULL
588 LOAD_FAST 0 (self)
590 LOAD_ATTR 26 (browser)
592 LOAD_ATTR 34 (new_context)
594 LOAD_CONST 22 (())
596 BUILD_MAP 0
598 LOAD_FAST 10 (context_kwargs)
600 DICT_MERGE 1
602 CALL_FUNCTION_EX 1 (keyword and positional arguments)
604 GET_AWAITABLE 0
606 LOAD_CONST 3 (None)
608 SEND 3 (to 614)
610 YIELD_VALUE
612 JUMP_BACKWARD_NO_INTERRUPT 4 (to 608)
614 LOAD_FAST 0 (self)
616 STORE_ATTR 25 (context)

618 LOAD_FAST 0 (self)
620 LOAD_METHOD 27 (_bind_single_page_policy)
622 CALL 0
624 GET_AWAITABLE 0
626 LOAD_CONST 3 (None)
628 SEND 3 (to 634)
630 YIELD_VALUE
632 JUMP_BACKWARD_NO_INTERRUPT 4 (to 628)
634 POP_TOP

636 LOAD_FAST 0 (self)
638 LOAD_ATTR 25 (context)
640 LOAD_METHOD 28 (new_page)
642 CALL 0
644 GET_AWAITABLE 0
646 LOAD_CONST 3 (None)
648 SEND 3 (to 654)
650 YIELD_VALUE
652 JUMP_BACKWARD_NO_INTERRUPT 4 (to 648)
654 LOAD_FAST 0 (self)
656 STORE_ATTR 29 (page)

658 LOAD_FAST 0 (self)
660 LOAD_ATTR 29 (page)
662 LOAD_METHOD 30 (set_default_timeout)
664 LOAD_GLOBAL 46 (settings)
666 LOAD_ATTR 31 (PLAYWRIGHT_TIMEOUT)
668 CALL 1
670 POP_TOP

672 LOAD_GLOBAL 1 (NULL + log_automation_step)
674 LOAD_FAST 0 (self)
676 LOAD_ATTR 1 (logger)
678 LOAD_CONST 1 ("BROWSER_INIT")
680 LOAD_CONST 21 ("STANDARD_MODE")
682 CALL 3
684 POP_TOP
686 LOAD_CONST 3 (None)
688 RETURN_VALUE


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("NAVIGATION")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_FAST 0 (self)
22 LOAD_ATTR 2 (page)
24 LOAD_METHOD 3 (goto)
26 LOAD_GLOBAL 8 (settings)
28 LOAD_ATTR 5 (CLOUDSKILL_REGISTER_URL)
30 CALL 1
32 GET_AWAITABLE 0
34 LOAD_CONST 3 (None)
36 SEND 3 (to 42)
38 YIELD_VALUE
40 JUMP_BACKWARD_NO_INTERRUPT 4 (to 36)
42 POP_TOP

44 LOAD_FAST 0 (self)
46 LOAD_ATTR 2 (page)
48 LOAD_METHOD 6 (wait_for_load_state)
50 LOAD_CONST 4 ("networkidle")
52 CALL 1
54 GET_AWAITABLE 0
56 LOAD_CONST 3 (None)
58 SEND 3 (to 64)
60 YIELD_VALUE
62 JUMP_BACKWARD_NO_INTERRUPT 4 (to 58)
64 POP_TOP

66 NOP

68 LOAD_FAST 0 (self)
70 LOAD_ATTR 2 (page)
72 LOAD_METHOD 7 (wait_for_selector)
74 LOAD_CONST 5 ("input[type='email'], input[name='email'], input[type='text']")
76 LOAD_CONST 6 (15000)
78 KW_NAMES 7 (('timeout',))
80 CALL 2
82 GET_AWAITABLE 0
84 LOAD_CONST 3 (None)
86 SEND 3 (to 92)
88 YIELD_VALUE
90 JUMP_BACKWARD_NO_INTERRUPT 4 (to 86)
92 POP_TOP
94 JUMP_FORWARD 133 (to 202)
96 PUSH_EXC_INFO

98 POP_TOP

100 LOAD_FAST 0 (self)
102 LOAD_ATTR 2 (page)
104 LOAD_METHOD 8 (query_selector)
106 LOAD_CONST 8 ("a:has-text('Sign up'), button:has-text('Sign up'), a:has-text('Register'), button:has-text('Register')")
108 CALL 1
110 GET_AWAITABLE 0
112 LOAD_CONST 3 (None)
114 SEND 3 (to 120)
116 YIELD_VALUE
118 JUMP_BACKWARD_NO_INTERRUPT 4 (to 114)
120 STORE_FAST 1 (sign_up_btn)

122 LOAD_FAST 1 (sign_up_btn)
124 POP_JUMP_FORWARD_IF_FALSE 92 (to 192)

126 LOAD_FAST 1 (sign_up_btn)
128 LOAD_METHOD 9 (click)
130 CALL 0
132 GET_AWAITABLE 0
134 LOAD_CONST 3 (None)
136 SEND 3 (to 142)
138 YIELD_VALUE
140 JUMP_BACKWARD_NO_INTERRUPT 4 (to 136)
142 POP_TOP

144 LOAD_FAST 0 (self)
146 LOAD_ATTR 2 (page)
148 LOAD_METHOD 6 (wait_for_load_state)
150 LOAD_CONST 4 ("networkidle")
152 CALL 1
154 GET_AWAITABLE 0
156 LOAD_CONST 3 (None)
158 SEND 3 (to 164)
160 YIELD_VALUE
162 JUMP_BACKWARD_NO_INTERRUPT 4 (to 158)
164 POP_TOP

166 LOAD_FAST 0 (self)
168 LOAD_ATTR 2 (page)
170 LOAD_METHOD 7 (wait_for_selector)
172 LOAD_CONST 5 ("input[type='email'], input[name='email'], input[type='text']")
174 LOAD_CONST 9 (10000)
176 KW_NAMES 7 (('timeout',))
178 CALL 2
180 GET_AWAITABLE 0
182 LOAD_CONST 3 (None)
184 SEND 3 (to 190)
186 YIELD_VALUE
188 JUMP_BACKWARD_NO_INTERRUPT 4 (to 184)
190 POP_TOP
192 POP_EXCEPT
194 JUMP_FORWARD 3 (to 202)
196 COPY 3
198 POP_EXCEPT
200 RERAISE 1

202 LOAD_GLOBAL 1 (NULL + log_automation_step)
204 LOAD_FAST 0 (self)
206 LOAD_ATTR 1 (logger)
208 LOAD_CONST 1 ("NAVIGATION")
210 LOAD_CONST 10 ("SUCCESS")
212 LOAD_CONST 11 ("url")
214 LOAD_FAST 0 (self)
216 LOAD_ATTR 2 (page)
218 LOAD_ATTR 10 (url)
220 BUILD_MAP 1
222 CALL 4
224 POP_TOP
226 LOAD_CONST 3 (None)
228 RETURN_VALUE
230 PUSH_EXC_INFO

232 LOAD_GLOBAL 22 (Exception)
234 CHECK_EXC_MATCH
236 POP_JUMP_FORWARD_IF_FALSE 44 (to 274)
238 STORE_FAST 2 (e)

240 LOAD_GLOBAL 1 (NULL + log_automation_step)
242 LOAD_FAST 0 (self)
244 LOAD_ATTR 1 (logger)
246 LOAD_CONST 1 ("NAVIGATION")
248 LOAD_CONST 12 ("ERROR")
250 LOAD_CONST 13 ("error")
252 LOAD_GLOBAL 25 (NULL + str)
254 LOAD_FAST 2 (e)
256 CALL 1
258 BUILD_MAP 1
260 CALL 4
262 POP_TOP

264 RAISE_VARARGS 0 (reraise)
266 LOAD_CONST 3 (None)
268 STORE_FAST 2 (e)
270 DELETE_FAST 2 (e)
272 RERAISE 1

274 RERAISE 0
276 COPY 3
278 POP_EXCEPT
280 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_DEREF 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("FORM_FILLING")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_CONST 3 ("\n            const selector = arguments[0];\n            const maxDepth = 5;\n            const queue = [{ root: document, depth: 0 }];\n            \n            while (queue.length) {\n                const { root, depth } = queue.shift();\n                try {\n                    const el = root.querySelector(selector);\n                    if (el) return el;\n                } catch (e) {}\n                \n                let nodes = [];\n                try { \n                    nodes = root.querySelectorAll('*'); \n                } catch (e) { \n                    nodes = []; \n                }\n                \n                for (const n of nodes) {\n                    if (n && n.shadowRoot && depth < maxDepth) {\n                        queue.push({ root: n.shadowRoot, depth: depth + 1 });\n                    }\n                }\n            }\n            return null;\n            ")
22 STORE_DEREF 16 (deep_fill_field)

24 LOAD_CONST 4 ("\n            const element = arguments[0];\n            const value = arguments[1];\n            \n            function setVal(el) {\n                if (!el) return false;\n                if (el.readOnly || el.disabled) return false;\n                \n                try { el.focus(); } catch(e) {}\n                try { el.value = ''; } catch(e) {}\n                try { el.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}\n                try { el.value = value; } catch(e) { return false; }\n                try { el.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}\n                try { el.dispatchEvent(new Event('change', { bubbles: true })); } catch(e) {}\n                return true;\n            }\n            \n            const tag = (element.tagName || '').toUpperCase();\n            if (tag === 'INPUT' || tag === 'TEXTAREA') {\n                return setVal(element);\n            }\n            \n            if (typeof element.value !== 'undefined') {\n                try { element.focus?.(); } catch(e) {}\n                try { element.value = value; } catch(e) {}\n                try { element.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}\n                try { element.dispatchEvent(new Event('change', { bubbles: true })); } catch(e) {}\n                return true;\n            }\n            \n            // Try shadow DOM\n            let inp = null;\n            if (element.shadowRoot) {\n                inp = element.shadowRoot.querySelector('input,textarea');\n                if (inp && setVal(inp)) return true;\n            }\n            \n            inp = element.querySelector?.('input,textarea') || null;\n            if (inp && setVal(inp)) return true;\n            \n            return false;\n            ")
26 STORE_DEREF 17 (deep_query_script)

28 LOAD_CLOSURE 15 (self)
30 LOAD_CLOSURE 0 (self)
32 BUILD_TUPLE 2
34 LOAD_CONST 5 (code object smart_fill_field)
36 MAKE_FUNCTION 8 (closure)
38 STORE_FAST 2 (smart_fill_field)

40 LOAD_CLOSURE 16 (deep_fill_field)
42 LOAD_CLOSURE 17 (deep_query_script)
44 LOAD_CLOSURE 0 (self)
46 BUILD_TUPLE 3
48 LOAD_CONST 6 (code object deep_fill_field)
50 MAKE_FUNCTION 8 (closure)
52 STORE_DEREF 15 (self)

54 LOAD_CONST 7 (False)

56 LOAD_CONST 7 (False)

58 LOAD_CONST 7 (False)

60 LOAD_CONST 7 (False)

62 LOAD_CONST 7 (False)

64 LOAD_CONST 7 (False)

66 LOAD_CONST 8 (('first_name', 'last_name', 'email', 'company', 'password', 'password_confirm'))
68 BUILD_CONST_KEY_MAP 6
70 STORE_DEREF 18 (fill_input_script)

72 BUILD_LIST 0
74 LOAD_CONST 9 (("input[name='user[first_name]']", "input[name='firstName']", "input[name='first_name']", "input[placeholder*='First name']", "input[placeholder*='First']", "input[id*='first']", "input[type='text']:first-of-type"))
76 LIST_EXTEND 1
78 STORE_FAST 3 (first_name_selectors)

80 PUSH_NULL
82 LOAD_FAST 2 (smart_fill_field)

84 LOAD_CONST 10 ("First name")
86 BUILD_LIST 1

88 LOAD_CONST 10 ("First name")
90 BUILD_LIST 1

92 LOAD_FAST 3 (first_name_selectors)

94 LOAD_FAST 1 (user_data)
96 LOAD_CONST 11 ("first_name")
98 BINARY_SUBSCR

100 LOAD_CONST 12 ("FIRST_NAME")
102 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
104 CALL 5
106 GET_AWAITABLE 0
108 LOAD_CONST 14 (None)
110 SEND 3 (to 116)
112 YIELD_VALUE
114 JUMP_BACKWARD_NO_INTERRUPT 4 (to 110)
116 LOAD_DEREF 18 (fill_input_script)
118 LOAD_CONST 11 ("first_name")
120 STORE_SUBSCR

122 BUILD_LIST 0
124 LOAD_CONST 15 (("input[name='user[last_name]']", "input[name='lastName']", "input[name='last_name']", "input[placeholder*='Last name']", "input[placeholder*='Last']", "input[id*='last']"))
126 LIST_EXTEND 1
128 STORE_FAST 4 (last_name_selectors)

130 PUSH_NULL
132 LOAD_FAST 2 (smart_fill_field)

134 LOAD_CONST 16 ("Last name")
136 BUILD_LIST 1

138 LOAD_CONST 16 ("Last name")
140 BUILD_LIST 1

142 LOAD_FAST 4 (last_name_selectors)

144 LOAD_FAST 1 (user_data)
146 LOAD_CONST 17 ("last_name")
148 BINARY_SUBSCR

150 LOAD_CONST 18 ("LAST_NAME")
152 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
154 CALL 5
156 GET_AWAITABLE 0
158 LOAD_CONST 14 (None)
160 SEND 3 (to 166)
162 YIELD_VALUE
164 JUMP_BACKWARD_NO_INTERRUPT 4 (to 160)
166 LOAD_DEREF 18 (fill_input_script)
168 LOAD_CONST 17 ("last_name")
170 STORE_SUBSCR

172 BUILD_LIST 0
174 LOAD_CONST 19 (("input[name='user[email]']", "input[name='email']", "input[type='email']", "input[placeholder*='Email']", "input[placeholder*='email']", "input[id*='email']"))
176 LIST_EXTEND 1
178 STORE_FAST 5 (email_selectors)

180 PUSH_NULL
182 LOAD_FAST 2 (smart_fill_field)

184 LOAD_CONST 20 ("Email")
186 BUILD_LIST 1

188 LOAD_CONST 20 ("Email")
190 BUILD_LIST 1

192 LOAD_FAST 5 (email_selectors)

194 LOAD_FAST 1 (user_data)
196 LOAD_CONST 21 ("email")
198 BINARY_SUBSCR

200 LOAD_CONST 22 ("EMAIL")
202 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
204 CALL 5
206 GET_AWAITABLE 0
208 LOAD_CONST 14 (None)
210 SEND 3 (to 216)
212 YIELD_VALUE
214 JUMP_BACKWARD_NO_INTERRUPT 4 (to 210)
216 LOAD_DEREF 18 (fill_input_script)
218 LOAD_CONST 21 ("email")
220 STORE_SUBSCR

222 BUILD_LIST 0
224 LOAD_CONST 23 (("input[name='user[company_name]']", "input[name='company']", "input[name='companyName']", "input[name='company_name']", "input[placeholder*='Company']", "input[placeholder*='company']", "input[id*='company']"))
226 LIST_EXTEND 1
228 STORE_FAST 6 (company_selectors)

230 PUSH_NULL
232 LOAD_FAST 2 (smart_fill_field)

234 LOAD_CONST 24 ("Company")
236 BUILD_LIST 1

238 LOAD_CONST 24 ("Company")
240 BUILD_LIST 1

242 LOAD_FAST 6 (company_selectors)

244 LOAD_FAST 1 (user_data)
246 LOAD_CONST 25 ("company")
248 BINARY_SUBSCR

250 LOAD_CONST 26 ("COMPANY")
252 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
254 CALL 5
256 GET_AWAITABLE 0
258 LOAD_CONST 14 (None)
260 SEND 3 (to 266)
262 YIELD_VALUE
264 JUMP_BACKWARD_NO_INTERRUPT 4 (to 260)
266 LOAD_DEREF 18 (fill_input_script)
268 LOAD_CONST 25 ("company")
270 STORE_SUBSCR

272 BUILD_LIST 0
274 LOAD_CONST 27 (("input[name='user[password]']", "input[name='password']", "input[type='password']:first-of-type", "input[id*='password']:not([id*='confirm'])", "input[placeholder*='Password']"))
276 LIST_EXTEND 1
278 STORE_FAST 7 (password_selectors)

280 PUSH_NULL
282 LOAD_FAST 2 (smart_fill_field)

284 LOAD_CONST 28 ("Password")
286 BUILD_LIST 1

288 LOAD_CONST 28 ("Password")
290 BUILD_LIST 1

292 LOAD_FAST 7 (password_selectors)

294 LOAD_FAST 1 (user_data)
296 LOAD_CONST 29 ("password")
298 BINARY_SUBSCR

300 LOAD_CONST 30 ("PASSWORD")
302 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
304 CALL 5
306 GET_AWAITABLE 0
308 LOAD_CONST 14 (None)
310 SEND 3 (to 316)
312 YIELD_VALUE
314 JUMP_BACKWARD_NO_INTERRUPT 4 (to 310)
316 LOAD_DEREF 18 (fill_input_script)
318 LOAD_CONST 29 ("password")
320 STORE_SUBSCR

322 BUILD_LIST 0
324 LOAD_CONST 31 (("input[name='user[password_confirmation]']", "input[name='password_confirmation']", "input[name='passwordConfirmation']", "input[name='confirmPassword']", "input[type='password']:last-of-type", "input[id*='confirm']", "input[placeholder*='Password confirmation']"))
326 LIST_EXTEND 1
328 STORE_FAST 8 (confirm_selectors)

330 PUSH_NULL
332 LOAD_FAST 2 (smart_fill_field)

334 LOAD_CONST 32 ("Password confirmation")
336 BUILD_LIST 1

338 LOAD_CONST 32 ("Password confirmation")
340 BUILD_LIST 1

342 LOAD_FAST 8 (confirm_selectors)

344 LOAD_FAST 1 (user_data)
346 LOAD_CONST 33 ("password_confirm")
348 BINARY_SUBSCR

350 LOAD_CONST 34 ("PASSWORD_CONFIRM")
352 KW_NAMES 13 (('labels', 'placeholders', 'selectors', 'value', 'field_name'))
354 CALL 5
356 GET_AWAITABLE 0
358 LOAD_CONST 14 (None)
360 SEND 3 (to 366)
362 YIELD_VALUE
364 JUMP_BACKWARD_NO_INTERRUPT 4 (to 360)
366 LOAD_DEREF 18 (fill_input_script)
368 LOAD_CONST 33 ("password_confirm")
370 STORE_SUBSCR

372 LOAD_DEREF 0 (self)
374 LOAD_METHOD 2 (_fill_birth_date)
376 CALL 0
378 GET_AWAITABLE 0
380 LOAD_CONST 14 (None)
382 SEND 3 (to 388)
384 YIELD_VALUE
386 JUMP_BACKWARD_NO_INTERRUPT 4 (to 382)
388 POP_TOP

390 LOAD_DEREF 0 (self)
392 LOAD_METHOD 3 (_handle_newsletter_checkbox)
394 CALL 0
396 GET_AWAITABLE 0
398 LOAD_CONST 14 (None)
400 SEND 3 (to 406)
402 YIELD_VALUE
404 JUMP_BACKWARD_NO_INTERRUPT 4 (to 400)
406 POP_TOP

408 NOP

410 LOAD_DEREF 0 (self)
412 LOAD_ATTR 4 (page)
414 LOAD_METHOD 5 (evaluate)

416 LOAD_CONST 35 ('\n                    (sk) => {\n                        try {\n                            const byKey = document.querySelector(`div.g-recaptcha[data-sitekey="${sk}"]`);\n                            const any = byKey || document.querySelector("div.g-recaptcha");\n                            if (any) { try { any.scrollIntoView({block:"center"}); } catch(e) {} }\n                            return !!any;\n                        } catch(e) { return false; }\n                    }\n                ')

418 LOAD_CONST 36 ("6LeOI8IUAAAAAPkHlMAE9NReCD_1WD81iYlBlCnV")
420 CALL 2
422 GET_AWAITABLE 0
424 LOAD_CONST 14 (None)
426 SEND 3 (to 432)
428 YIELD_VALUE
430 JUMP_BACKWARD_NO_INTERRUPT 4 (to 426)
432 POP_TOP

434 LOAD_GLOBAL 13 (NULL + asyncio)
436 LOAD_ATTR 7 (sleep)
438 LOAD_CONST 37 (0.2)
440 CALL 1
442 GET_AWAITABLE 0
444 LOAD_CONST 14 (None)
446 SEND 3 (to 452)
448 YIELD_VALUE
450 JUMP_BACKWARD_NO_INTERRUPT 4 (to 446)
452 POP_TOP
454 JUMP_FORWARD 16 (to 478)
456 PUSH_EXC_INFO

458 LOAD_GLOBAL 16 (Exception)
460 CHECK_EXC_MATCH
462 POP_JUMP_FORWARD_IF_FALSE 3 (to 470)
464 POP_TOP

466 POP_EXCEPT
468 JUMP_FORWARD 4 (to 478)

470 RERAISE 0
472 COPY 3
474 POP_EXCEPT
476 RERAISE 1

478 NOP

480 LOAD_DEREF 0 (self)
482 LOAD_METHOD 9 (_scroll_to_recaptcha)
484 LOAD_CONST 38 (5)
486 LOAD_CONST 39 (True)
488 LOAD_CONST 39 (True)
490 KW_NAMES 40 (('max_steps', 'fast', 'skip_fallback'))
492 CALL 3
494 GET_AWAITABLE 0
496 LOAD_CONST 14 (None)
498 SEND 3 (to 504)
500 YIELD_VALUE
502 JUMP_BACKWARD_NO_INTERRUPT 4 (to 498)
504 POP_TOP
506 JUMP_FORWARD 16 (to 530)
508 PUSH_EXC_INFO

510 LOAD_GLOBAL 16 (Exception)
512 CHECK_EXC_MATCH
514 POP_JUMP_FORWARD_IF_FALSE 3 (to 522)
516 POP_TOP

518 POP_EXCEPT
520 JUMP_FORWARD 4 (to 530)

522 RERAISE 0
524 COPY 3
526 POP_EXCEPT
528 RERAISE 1

530 LOAD_CONST 41 (code object <listcomp>)
532 MAKE_FUNCTION 0 (No arguments)
534 LOAD_DEREF 18 (fill_input_script)
536 LOAD_METHOD 10 (items)
538 CALL 0
540 GET_ITER
542 CALL 0
544 STORE_FAST 9 (failed_fields)

546 LOAD_CONST 42 (code object <listcomp>)
548 MAKE_FUNCTION 0 (No arguments)
550 LOAD_DEREF 18 (fill_input_script)
552 LOAD_METHOD 10 (items)
554 CALL 0
556 GET_ITER
558 CALL 0
560 STORE_FAST 10 (successful_fields)

562 LOAD_GLOBAL 1 (NULL + log_automation_step)
564 LOAD_DEREF 0 (self)
566 LOAD_ATTR 1 (logger)
568 LOAD_CONST 43 ("FORM_VALIDATION")

570 LOAD_CONST 44 ("SUMMARY")
572 LOAD_FAST 10 (successful_fields)

574 LOAD_FAST 9 (failed_fields)

576 LOAD_GLOBAL 23 (NULL + len)
578 LOAD_FAST 10 (successful_fields)
580 CALL 1
582 FORMAT_VALUE 0
584 LOAD_CONST 45 ("/")
586 LOAD_GLOBAL 23 (NULL + len)
588 LOAD_DEREF 18 (fill_input_script)
590 CALL 1
592 FORMAT_VALUE 0
594 BUILD_STRING 3

596 LOAD_CONST 46 (('successful_fields', 'failed_fields', 'success_rate'))
598 BUILD_CONST_KEY_MAP 3
600 CALL 4
602 POP_TOP

604 BUILD_LIST 0
606 LOAD_CONST 47 (('first_name', 'email', 'password'))
608 LIST_EXTEND 1
610 STORE_FAST 11 (critical_fields)

612 LOAD_CLOSURE 18 (fill_input_script)
614 BUILD_TUPLE 1
616 LOAD_CONST 48 (code object <listcomp>)
618 MAKE_FUNCTION 8 (closure)
620 LOAD_FAST 11 (critical_fields)
622 GET_ITER
624 CALL 0
626 STORE_FAST 12 (critical_failed)

628 LOAD_FAST 12 (critical_failed)
630 POP_JUMP_FORWARD_IF_FALSE 64 (to 676)

632 LOAD_CONST 49 ("Critical fields tidak terisi: ")
634 LOAD_CONST 50 (", ")
636 LOAD_METHOD 12 (join)
638 LOAD_FAST 12 (critical_failed)
640 CALL 1
642 FORMAT_VALUE 0
644 BUILD_STRING 2
646 STORE_FAST 13 (error_msg)

648 LOAD_GLOBAL 1 (NULL + log_automation_step)
650 LOAD_DEREF 0 (self)
652 LOAD_ATTR 1 (logger)
654 LOAD_CONST 1 ("FORM_FILLING")
656 LOAD_CONST 51 ("CRITICAL_ERROR")
658 LOAD_CONST 52 ("failed_critical_fields")
660 LOAD_FAST 12 (critical_failed)
662 BUILD_MAP 1
664 CALL 4
666 POP_TOP

668 LOAD_GLOBAL 17 (NULL + Exception)
670 LOAD_FAST 13 (error_msg)
672 CALL 1
674 RAISE_VARARGS 1 (exception instance)

676 LOAD_GLOBAL 23 (NULL + len)
678 LOAD_FAST 9 (failed_fields)
680 CALL 1
682 LOAD_CONST 53 (2)
684 COMPARE_OP 4 (>)
686 POP_JUMP_FORWARD_IF_FALSE 64 (to 732)

688 LOAD_CONST 54 ("Terlalu banyak field yang gagal diisi: ")
690 LOAD_CONST 50 (", ")
692 LOAD_METHOD 12 (join)
694 LOAD_FAST 9 (failed_fields)
696 CALL 1
698 FORMAT_VALUE 0
700 BUILD_STRING 2
702 STORE_FAST 13 (error_msg)

704 LOAD_GLOBAL 1 (NULL + log_automation_step)
706 LOAD_DEREF 0 (self)
708 LOAD_ATTR 1 (logger)
710 LOAD_CONST 1 ("FORM_FILLING")
712 LOAD_CONST 55 ("ERROR")
714 LOAD_CONST 56 ("failed_fields")
716 LOAD_FAST 9 (failed_fields)
718 BUILD_MAP 1
720 CALL 4
722 POP_TOP

724 LOAD_GLOBAL 17 (NULL + Exception)
726 LOAD_FAST 13 (error_msg)
728 CALL 1
730 RAISE_VARARGS 1 (exception instance)

732 LOAD_GLOBAL 1 (NULL + log_automation_step)
734 LOAD_DEREF 0 (self)
736 LOAD_ATTR 1 (logger)
738 LOAD_CONST 1 ("FORM_FILLING")

740 LOAD_CONST 57 ("SUCCESS")
742 LOAD_FAST 10 (successful_fields)

744 LOAD_FAST 9 (failed_fields)

746 LOAD_CONST 58 (('filled_fields', 'skipped_fields'))
748 BUILD_CONST_KEY_MAP 2
750 CALL 4
752 POP_TOP
754 LOAD_CONST 14 (None)
756 RETURN_VALUE
758 PUSH_EXC_INFO

760 LOAD_GLOBAL 16 (Exception)
762 CHECK_EXC_MATCH
764 POP_JUMP_FORWARD_IF_FALSE 44 (to 802)
766 STORE_FAST 14 (e)

768 LOAD_GLOBAL 1 (NULL + log_automation_step)
770 LOAD_DEREF 0 (self)
772 LOAD_ATTR 1 (logger)
774 LOAD_CONST 1 ("FORM_FILLING")
776 LOAD_CONST 55 ("ERROR")
778 LOAD_CONST 59 ("error")
780 LOAD_GLOBAL 27 (NULL + str)
782 LOAD_FAST 14 (e)
784 CALL 1
786 BUILD_MAP 1
788 CALL 4
790 POP_TOP

792 RAISE_VARARGS 0 (reraise)
794 LOAD_CONST 14 (None)
796 STORE_FAST 14 (e)
798 DELETE_FAST 14 (e)
800 RERAISE 1

802 RERAISE 0
804 COPY 3
806 POP_EXCEPT
808 RERAISE 1

0 COPY_FREE_VARS 2

2 RETURN_GENERATOR
4 POP_TOP

6 LOAD_FAST 0 (labels)
8 JUMP_IF_TRUE_OR_POP 1 (to 12)
10 BUILD_LIST 0
12 GET_ITER
14 FOR_ITER 348 (to 314)
16 STORE_FAST 5 (lbl)

18 NOP

20 LOAD_DEREF 11 (self)
22 LOAD_ATTR 0 (page)
24 LOAD_METHOD 1 (get_by_label)
26 LOAD_FAST 5 (lbl)
28 CALL 1
30 STORE_FAST 6 (base)

32 LOAD_FAST 6 (base)
34 LOAD_METHOD 2 (count)
36 CALL 0
38 GET_AWAITABLE 0
40 LOAD_CONST 0 (None)
42 SEND 3 (to 48)
44 YIELD_VALUE
46 JUMP_BACKWARD_NO_INTERRUPT 4 (to 42)
48 LOAD_CONST 1 (0)
50 COMPARE_OP 4 (>)
52 POP_JUMP_FORWARD_IF_FALSE 221 (to 242)

54 LOAD_FAST 6 (base)
56 LOAD_ATTR 3 (first)
58 STORE_FAST 7 (locator)

60 LOAD_FAST 7 (locator)
62 LOAD_METHOD 4 (scroll_into_view_if_needed)
64 CALL 0
66 GET_AWAITABLE 0
68 LOAD_CONST 0 (None)
70 SEND 3 (to 76)
72 YIELD_VALUE
74 JUMP_BACKWARD_NO_INTERRUPT 4 (to 70)
76 POP_TOP

78 LOAD_FAST 7 (locator)
80 LOAD_METHOD 5 (wait_for)
82 LOAD_CONST 2 ("visible")
84 LOAD_CONST 3 (5000)
86 KW_NAMES 4 (('state', 'timeout'))
88 CALL 2
90 GET_AWAITABLE 0
92 LOAD_CONST 0 (None)
94 SEND 3 (to 100)
96 YIELD_VALUE
98 JUMP_BACKWARD_NO_INTERRUPT 4 (to 94)
100 POP_TOP

102 LOAD_FAST 7 (locator)
104 LOAD_METHOD 6 (click)
106 CALL 0
108 GET_AWAITABLE 0
110 LOAD_CONST 0 (None)
112 SEND 3 (to 118)
114 YIELD_VALUE
116 JUMP_BACKWARD_NO_INTERRUPT 4 (to 112)
118 POP_TOP

120 LOAD_FAST 7 (locator)
122 LOAD_METHOD 7 (fill)
124 LOAD_FAST 3 (value)
126 CALL 1
128 GET_AWAITABLE 0
130 LOAD_CONST 0 (None)
132 SEND 3 (to 138)
134 YIELD_VALUE
136 JUMP_BACKWARD_NO_INTERRUPT 4 (to 132)
138 POP_TOP

140 LOAD_GLOBAL 17 (NULL + asyncio)
142 LOAD_ATTR 9 (sleep)
144 LOAD_CONST 5 (0.1)
146 CALL 1
148 GET_AWAITABLE 0
150 LOAD_CONST 0 (None)
152 SEND 3 (to 158)
154 YIELD_VALUE
156 JUMP_BACKWARD_NO_INTERRUPT 4 (to 152)
158 POP_TOP

160 NOP

162 LOAD_FAST 7 (locator)
164 LOAD_METHOD 10 (input_value)
166 CALL 0
168 GET_AWAITABLE 0
170 LOAD_CONST 0 (None)
172 SEND 3 (to 178)
174 YIELD_VALUE
176 JUMP_BACKWARD_NO_INTERRUPT 4 (to 172)
178 LOAD_FAST 3 (value)
180 COMPARE_OP 2 (==)
182 POP_JUMP_FORWARD_IF_FALSE 32 (to 218)

184 LOAD_GLOBAL 23 (NULL + log_automation_step)
186 LOAD_DEREF 11 (self)
188 LOAD_ATTR 12 (logger)
190 LOAD_FAST 4 (field_name)
192 FORMAT_VALUE 0
194 LOAD_CONST 6 ("_FILLED")
196 BUILD_STRING 2
198 LOAD_CONST 7 ("SUCCESS")
200 LOAD_CONST 8 ("get_by_label")
202 LOAD_FAST 5 (lbl)
204 LOAD_CONST 9 (('method', 'label'))
206 BUILD_CONST_KEY_MAP 2
208 CALL 4
210 POP_TOP

212 POP_TOP
214 LOAD_CONST 10 (True)
216 RETURN_VALUE

218 JUMP_FORWARD 16 (to 242)
220 PUSH_EXC_INFO

222 LOAD_GLOBAL 26 (Exception)
224 CHECK_EXC_MATCH
226 POP_JUMP_FORWARD_IF_FALSE 3 (to 234)
228 POP_TOP

230 POP_EXCEPT
232 JUMP_FORWARD 4 (to 242)

234 RERAISE 0
236 COPY 3
238 POP_EXCEPT
240 RERAISE 1
242 JUMP_BACKWARD 283 (to 14)
244 PUSH_EXC_INFO

246 LOAD_GLOBAL 26 (Exception)
248 CHECK_EXC_MATCH
250 POP_JUMP_FORWARD_IF_FALSE 54 (to 306)
252 STORE_FAST 8 (e)

254 LOAD_GLOBAL 23 (NULL + log_automation_step)
256 LOAD_DEREF 11 (self)
258 LOAD_ATTR 12 (logger)
260 LOAD_FAST 4 (field_name)
262 FORMAT_VALUE 0
264 LOAD_CONST 11 ("_ATTEMPT")
266 BUILD_STRING 2
268 LOAD_CONST 12 ("FAILED")
270 LOAD_CONST 8 ("get_by_label")
272 LOAD_FAST 5 (lbl)
274 LOAD_GLOBAL 29 (NULL + str)
276 LOAD_FAST 8 (e)
278 CALL 1
280 LOAD_CONST 13 (('method', 'label', 'error'))
282 BUILD_CONST_KEY_MAP 3
284 CALL 4
286 POP_TOP

288 POP_EXCEPT
290 LOAD_CONST 0 (None)
292 STORE_FAST 8 (e)
294 DELETE_FAST 8 (e)
296 JUMP_BACKWARD 342 (to 14)
298 LOAD_CONST 0 (None)
300 STORE_FAST 8 (e)
302 DELETE_FAST 8 (e)
304 RERAISE 1

306 RERAISE 0
308 COPY 3
310 POP_EXCEPT
312 RERAISE 1

314 LOAD_FAST 1 (placeholders)
316 JUMP_IF_TRUE_OR_POP 1 (to 320)
318 BUILD_LIST 0
320 GET_ITER
322 FOR_ITER 348 (to 622)
324 STORE_FAST 9 (ph)

326 NOP

328 LOAD_DEREF 11 (self)
330 LOAD_ATTR 0 (page)
332 LOAD_METHOD 15 (get_by_placeholder)
334 LOAD_FAST 9 (ph)
336 CALL 1
338 STORE_FAST 6 (base)

340 LOAD_FAST 6 (base)
342 LOAD_METHOD 2 (count)
344 CALL 0
346 GET_AWAITABLE 0
348 LOAD_CONST 0 (None)
350 SEND 3 (to 356)
352 YIELD_VALUE
354 JUMP_BACKWARD_NO_INTERRUPT 4 (to 350)
356 LOAD_CONST 1 (0)
358 COMPARE_OP 4 (>)
360 POP_JUMP_FORWARD_IF_FALSE 221 (to 550)

362 LOAD_FAST 6 (base)
364 LOAD_ATTR 3 (first)
366 STORE_FAST 7 (locator)

368 LOAD_FAST 7 (locator)
370 LOAD_METHOD 4 (scroll_into_view_if_needed)
372 CALL 0
374 GET_AWAITABLE 0
376 LOAD_CONST 0 (None)
378 SEND 3 (to 384)
380 YIELD_VALUE
382 JUMP_BACKWARD_NO_INTERRUPT 4 (to 378)
384 POP_TOP

386 LOAD_FAST 7 (locator)
388 LOAD_METHOD 5 (wait_for)
390 LOAD_CONST 2 ("visible")
392 LOAD_CONST 3 (5000)
394 KW_NAMES 4 (('state', 'timeout'))
396 CALL 2
398 GET_AWAITABLE 0
400 LOAD_CONST 0 (None)
402 SEND 3 (to 408)
404 YIELD_VALUE
406 JUMP_BACKWARD_NO_INTERRUPT 4 (to 402)
408 POP_TOP

410 LOAD_FAST 7 (locator)
412 LOAD_METHOD 6 (click)
414 CALL 0
416 GET_AWAITABLE 0
418 LOAD_CONST 0 (None)
420 SEND 3 (to 426)
422 YIELD_VALUE
424 JUMP_BACKWARD_NO_INTERRUPT 4 (to 420)
426 POP_TOP

428 LOAD_FAST 7 (locator)
430 LOAD_METHOD 7 (fill)
432 LOAD_FAST 3 (value)
434 CALL 1
436 GET_AWAITABLE 0
438 LOAD_CONST 0 (None)
440 SEND 3 (to 446)
442 YIELD_VALUE
444 JUMP_BACKWARD_NO_INTERRUPT 4 (to 440)
446 POP_TOP

448 LOAD_GLOBAL 17 (NULL + asyncio)
450 LOAD_ATTR 9 (sleep)
452 LOAD_CONST 5 (0.1)
454 CALL 1
456 GET_AWAITABLE 0
458 LOAD_CONST 0 (None)
460 SEND 3 (to 466)
462 YIELD_VALUE
464 JUMP_BACKWARD_NO_INTERRUPT 4 (to 460)
466 POP_TOP

468 NOP

470 LOAD_FAST 7 (locator)
472 LOAD_METHOD 10 (input_value)
474 CALL 0
476 GET_AWAITABLE 0
478 LOAD_CONST 0 (None)
480 SEND 3 (to 486)
482 YIELD_VALUE
484 JUMP_BACKWARD_NO_INTERRUPT 4 (to 480)
486 LOAD_FAST 3 (value)
488 COMPARE_OP 2 (==)
490 POP_JUMP_FORWARD_IF_FALSE 32 (to 526)

492 LOAD_GLOBAL 23 (NULL + log_automation_step)
494 LOAD_DEREF 11 (self)
496 LOAD_ATTR 12 (logger)
498 LOAD_FAST 4 (field_name)
500 FORMAT_VALUE 0
502 LOAD_CONST 6 ("_FILLED")
504 BUILD_STRING 2
506 LOAD_CONST 7 ("SUCCESS")
508 LOAD_CONST 14 ("get_by_placeholder")
510 LOAD_FAST 9 (ph)
512 LOAD_CONST 15 (('method', 'placeholder'))
514 BUILD_CONST_KEY_MAP 2
516 CALL 4
518 POP_TOP

520 POP_TOP
522 LOAD_CONST 10 (True)
524 RETURN_VALUE

526 JUMP_FORWARD 16 (to 550)
528 PUSH_EXC_INFO

530 LOAD_GLOBAL 26 (Exception)
532 CHECK_EXC_MATCH
534 POP_JUMP_FORWARD_IF_FALSE 3 (to 542)
536 POP_TOP

538 POP_EXCEPT
540 JUMP_FORWARD 4 (to 550)

542 RERAISE 0
544 COPY 3
546 POP_EXCEPT
548 RERAISE 1
550 JUMP_BACKWARD 283 (to 322)
552 PUSH_EXC_INFO

554 LOAD_GLOBAL 26 (Exception)
556 CHECK_EXC_MATCH
558 POP_JUMP_FORWARD_IF_FALSE 54 (to 614)
560 STORE_FAST 8 (e)

562 LOAD_GLOBAL 23 (NULL + log_automation_step)
564 LOAD_DEREF 11 (self)
566 LOAD_ATTR 12 (logger)
568 LOAD_FAST 4 (field_name)
570 FORMAT_VALUE 0
572 LOAD_CONST 11 ("_ATTEMPT")
574 BUILD_STRING 2
576 LOAD_CONST 12 ("FAILED")
578 LOAD_CONST 14 ("get_by_placeholder")
580 LOAD_FAST 9 (ph)
582 LOAD_GLOBAL 29 (NULL + str)
584 LOAD_FAST 8 (e)
586 CALL 1
588 LOAD_CONST 16 (('method', 'placeholder', 'error'))
590 BUILD_CONST_KEY_MAP 3
592 CALL 4
594 POP_TOP

596 POP_EXCEPT
598 LOAD_CONST 0 (None)
600 STORE_FAST 8 (e)
602 DELETE_FAST 8 (e)
604 JUMP_BACKWARD 342 (to 322)
606 LOAD_CONST 0 (None)
608 STORE_FAST 8 (e)
610 DELETE_FAST 8 (e)
612 RERAISE 1

614 RERAISE 0
616 COPY 3
618 POP_EXCEPT
620 RERAISE 1

622 PUSH_NULL
624 LOAD_DEREF 10 (deep_fill_field)
626 LOAD_FAST 2 (selectors)
628 LOAD_FAST 3 (value)
630 LOAD_FAST 4 (field_name)
632 CALL 3
634 GET_AWAITABLE 0
636 LOAD_CONST 0 (None)
638 SEND 3 (to 644)
640 YIELD_VALUE
642 JUMP_BACKWARD_NO_INTERRUPT 4 (to 638)
644 RETURN_VALUE

0 COPY_FREE_VARS 3

2 RETURN_GENERATOR
4 POP_TOP

6 LOAD_FAST 0 (field_selectors)
8 GET_ITER
10 FOR_ITER 624 (to 578)
12 STORE_FAST 3 (selector)

14 NOP

16 LOAD_DEREF 13 (self)
18 LOAD_ATTR 0 (page)
20 LOAD_METHOD 1 (locator)
22 LOAD_FAST 3 (selector)
24 CALL 1
26 STORE_FAST 4 (base_loc)

28 LOAD_FAST 4 (base_loc)
30 LOAD_METHOD 2 (count)
32 CALL 0
34 GET_AWAITABLE 0
36 LOAD_CONST 0 (None)
38 SEND 3 (to 44)
40 YIELD_VALUE
42 JUMP_BACKWARD_NO_INTERRUPT 4 (to 38)
44 LOAD_CONST 1 (0)
46 COMPARE_OP 4 (>)
48 POP_JUMP_FORWARD_IF_FALSE 361 (to 392)

50 LOAD_FAST 4 (base_loc)
52 LOAD_ATTR 3 (first)
54 STORE_FAST 5 (locator)

56 NOP

58 LOAD_FAST 5 (locator)
60 LOAD_METHOD 4 (fill)
62 LOAD_CONST 2 ("")
64 CALL 1
66 GET_AWAITABLE 0
68 LOAD_CONST 0 (None)
70 SEND 3 (to 76)
72 YIELD_VALUE
74 JUMP_BACKWARD_NO_INTERRUPT 4 (to 70)
76 POP_TOP
78 JUMP_FORWARD 16 (to 102)
80 PUSH_EXC_INFO

82 LOAD_GLOBAL 10 (Exception)
84 CHECK_EXC_MATCH
86 POP_JUMP_FORWARD_IF_FALSE 3 (to 94)
88 POP_TOP

90 POP_EXCEPT
92 JUMP_FORWARD 4 (to 102)

94 RERAISE 0
96 COPY 3
98 POP_EXCEPT
100 RERAISE 1

102 LOAD_FAST 5 (locator)
104 LOAD_METHOD 6 (click)
106 LOAD_CONST 3 (True)
108 KW_NAMES 4 (('force',))
110 CALL 1
112 GET_AWAITABLE 0
114 LOAD_CONST 0 (None)
116 SEND 3 (to 122)
118 YIELD_VALUE
120 JUMP_BACKWARD_NO_INTERRUPT 4 (to 116)
122 POP_TOP

124 LOAD_FAST 5 (locator)
126 LOAD_METHOD 4 (fill)
128 LOAD_FAST 1 (value)
130 CALL 1
132 GET_AWAITABLE 0
134 LOAD_CONST 0 (None)
136 SEND 3 (to 142)
138 YIELD_VALUE
140 JUMP_BACKWARD_NO_INTERRUPT 4 (to 136)
142 POP_TOP

144 LOAD_GLOBAL 15 (NULL + asyncio)
146 LOAD_ATTR 8 (sleep)
148 LOAD_CONST 5 (0.2)
150 CALL 1
152 GET_AWAITABLE 0
154 LOAD_CONST 0 (None)
156 SEND 3 (to 162)
158 YIELD_VALUE
160 JUMP_BACKWARD_NO_INTERRUPT 4 (to 156)
162 POP_TOP

164 NOP

166 LOAD_FAST 5 (locator)
168 LOAD_METHOD 9 (input_value)
170 CALL 0
172 GET_AWAITABLE 0
174 LOAD_CONST 0 (None)
176 SEND 3 (to 182)
178 YIELD_VALUE
180 JUMP_BACKWARD_NO_INTERRUPT 4 (to 176)
182 STORE_FAST 6 (filled_value)
184 JUMP_FORWARD 18 (to 212)
186 PUSH_EXC_INFO

188 LOAD_GLOBAL 10 (Exception)
190 CHECK_EXC_MATCH
192 POP_JUMP_FORWARD_IF_FALSE 5 (to 204)
194 POP_TOP

196 LOAD_CONST 2 ("")
198 STORE_FAST 6 (filled_value)
200 POP_EXCEPT
202 JUMP_FORWARD 4 (to 212)

204 RERAISE 0
206 COPY 3
208 POP_EXCEPT
210 RERAISE 1

212 LOAD_FAST 6 (filled_value)
214 LOAD_FAST 1 (value)
216 COMPARE_OP 2 (==)
218 POP_JUMP_FORWARD_IF_FALSE 33 (to 256)

220 LOAD_GLOBAL 21 (NULL + log_automation_step)
222 LOAD_DEREF 13 (self)
224 LOAD_ATTR 11 (logger)
226 LOAD_FAST 2 (field_name)
228 FORMAT_VALUE 0
230 LOAD_CONST 6 ("_FILLED")
232 BUILD_STRING 2
234 LOAD_CONST 7 ("SUCCESS")
236 LOAD_FAST 3 (selector)
238 LOAD_CONST 8 ("locator_fill")
240 LOAD_FAST 6 (filled_value)
242 LOAD_CONST 9 (('selector', 'method', 'value'))
244 BUILD_CONST_KEY_MAP 3
246 CALL 4
248 POP_TOP

250 POP_TOP
252 LOAD_CONST 3 (True)
254 RETURN_VALUE

256 LOAD_FAST 5 (locator)
258 LOAD_METHOD 12 (element_handle)
260 CALL 0
262 GET_AWAITABLE 0
264 LOAD_CONST 0 (None)
266 SEND 3 (to 272)
268 YIELD_VALUE
270 JUMP_BACKWARD_NO_INTERRUPT 4 (to 266)
272 STORE_FAST 7 (handle)

274 LOAD_FAST 7 (handle)
276 POP_JUMP_FORWARD_IF_FALSE 115 (to 392)

278 LOAD_DEREF 13 (self)
280 LOAD_ATTR 0 (page)
282 LOAD_METHOD 13 (evaluate)
284 LOAD_DEREF 12 (fill_input_script)
286 LOAD_FAST 7 (handle)
288 LOAD_FAST 1 (value)
290 CALL 3
292 GET_AWAITABLE 0
294 LOAD_CONST 0 (None)
296 SEND 3 (to 302)
298 YIELD_VALUE
300 JUMP_BACKWARD_NO_INTERRUPT 4 (to 296)
302 STORE_FAST 8 (result)

304 LOAD_FAST 8 (result)
306 POP_JUMP_FORWARD_IF_FALSE 79 (to 392)

308 NOP

310 LOAD_FAST 5 (locator)
312 LOAD_METHOD 9 (input_value)
314 CALL 0
316 GET_AWAITABLE 0
318 LOAD_CONST 0 (None)
320 SEND 3 (to 326)
322 YIELD_VALUE
324 JUMP_BACKWARD_NO_INTERRUPT 4 (to 320)
326 STORE_FAST 6 (filled_value)
328 JUMP_FORWARD 18 (to 356)
330 PUSH_EXC_INFO

332 LOAD_GLOBAL 10 (Exception)
334 CHECK_EXC_MATCH
336 POP_JUMP_FORWARD_IF_FALSE 5 (to 348)
338 POP_TOP

340 LOAD_FAST 1 (value)
342 STORE_FAST 6 (filled_value)
344 POP_EXCEPT
346 JUMP_FORWARD 4 (to 356)

348 RERAISE 0
350 COPY 3
352 POP_EXCEPT
354 RERAISE 1

356 LOAD_GLOBAL 21 (NULL + log_automation_step)
358 LOAD_DEREF 13 (self)
360 LOAD_ATTR 11 (logger)
362 LOAD_FAST 2 (field_name)
364 FORMAT_VALUE 0
366 LOAD_CONST 6 ("_FILLED")
368 BUILD_STRING 2
370 LOAD_CONST 7 ("SUCCESS")
372 LOAD_FAST 3 (selector)
374 LOAD_CONST 10 ("locator_script")
376 LOAD_FAST 6 (filled_value)
378 LOAD_CONST 9 (('selector', 'method', 'value'))
380 BUILD_CONST_KEY_MAP 3
382 CALL 4
384 POP_TOP

386 POP_TOP
388 LOAD_CONST 3 (True)
390 RETURN_VALUE

392 LOAD_DEREF 13 (self)
394 LOAD_ATTR 0 (page)
396 LOAD_METHOD 14 (evaluate_handle)
398 LOAD_DEREF 11 (deep_query_script)
400 LOAD_FAST 3 (selector)
402 CALL 2
404 GET_AWAITABLE 0
406 LOAD_CONST 0 (None)
408 SEND 3 (to 414)
410 YIELD_VALUE
412 JUMP_BACKWARD_NO_INTERRUPT 4 (to 408)
414 STORE_FAST 7 (handle)

416 LOAD_DEREF 13 (self)
418 LOAD_ATTR 0 (page)
420 LOAD_METHOD 13 (evaluate)
422 LOAD_CONST 11 ("el => el === null")
424 LOAD_FAST 7 (handle)
426 CALL 2
428 GET_AWAITABLE 0
430 LOAD_CONST 0 (None)
432 SEND 3 (to 438)
434 YIELD_VALUE
436 JUMP_BACKWARD_NO_INTERRUPT 4 (to 432)
438 STORE_FAST 9 (is_null)

440 LOAD_FAST 9 (is_null)
442 POP_JUMP_FORWARD_IF_TRUE 68 (to 508)

444 LOAD_DEREF 13 (self)
446 LOAD_ATTR 0 (page)
448 LOAD_METHOD 13 (evaluate)
450 LOAD_DEREF 12 (fill_input_script)
452 LOAD_FAST 7 (handle)
454 LOAD_FAST 1 (value)
456 CALL 3
458 GET_AWAITABLE 0
460 LOAD_CONST 0 (None)
462 SEND 3 (to 468)
464 YIELD_VALUE
466 JUMP_BACKWARD_NO_INTERRUPT 4 (to 462)
468 STORE_FAST 8 (result)

470 LOAD_FAST 8 (result)
472 POP_JUMP_FORWARD_IF_FALSE 32 (to 508)

474 LOAD_GLOBAL 21 (NULL + log_automation_step)
476 LOAD_DEREF 13 (self)
478 LOAD_ATTR 11 (logger)
480 LOAD_FAST 2 (field_name)
482 FORMAT_VALUE 0
484 LOAD_CONST 6 ("_FILLED")
486 BUILD_STRING 2
488 LOAD_CONST 7 ("SUCCESS")
490 LOAD_FAST 3 (selector)
492 LOAD_CONST 12 ("deep_query")
494 LOAD_CONST 13 (('selector', 'method'))
496 BUILD_CONST_KEY_MAP 2
498 CALL 4
500 POP_TOP

502 POP_TOP
504 LOAD_CONST 3 (True)
506 RETURN_VALUE
508 JUMP_BACKWARD 560 (to 10)
510 PUSH_EXC_INFO

512 LOAD_GLOBAL 10 (Exception)
514 CHECK_EXC_MATCH
516 POP_JUMP_FORWARD_IF_FALSE 53 (to 570)
518 STORE_FAST 10 (e)

520 LOAD_GLOBAL 21 (NULL + log_automation_step)
522 LOAD_DEREF 13 (self)
524 LOAD_ATTR 11 (logger)
526 LOAD_FAST 2 (field_name)
528 FORMAT_VALUE 0
530 LOAD_CONST 14 ("_ATTEMPT")
532 BUILD_STRING 2
534 LOAD_CONST 15 ("FAILED")
536 LOAD_FAST 3 (selector)
538 LOAD_GLOBAL 31 (NULL + str)
540 LOAD_FAST 10 (e)
542 CALL 1
544 LOAD_CONST 16 (('selector', 'error'))
546 BUILD_CONST_KEY_MAP 2
548 CALL 4
550 POP_TOP

552 POP_EXCEPT
554 LOAD_CONST 0 (None)
556 STORE_FAST 10 (e)
558 DELETE_FAST 10 (e)
560 JUMP_BACKWARD 618 (to 10)
562 LOAD_CONST 0 (None)
564 STORE_FAST 10 (e)
566 DELETE_FAST 10 (e)
568 RERAISE 1

570 RERAISE 0
572 COPY 3
574 POP_EXCEPT
576 RERAISE 1

578 LOAD_GLOBAL 21 (NULL + log_automation_step)
580 LOAD_DEREF 13 (self)
582 LOAD_ATTR 11 (logger)
584 LOAD_FAST 2 (field_name)
586 FORMAT_VALUE 0
588 LOAD_CONST 6 ("_FILLED")
590 BUILD_STRING 2
592 LOAD_CONST 15 ("FAILED")
594 LOAD_CONST 17 ("reason")
596 LOAD_CONST 18 ("No working selector found")
598 BUILD_MAP 1
600 CALL 4
602 POP_TOP

604 LOAD_CONST 19 (False)
606 RETURN_VALUE


0 BUILD_LIST 0
2 LOAD_FAST 0 (.0)
4 FOR_ITER 9 (to 22)
6 UNPACK_SEQUENCE 2
8 STORE_FAST 1 (field)
10 STORE_FAST 2 (success)
12 LOAD_FAST 2 (success)
14 POP_JUMP_BACKWARD_IF_TRUE 7 (to 4)
16 LOAD_FAST 1 (field)
18 LIST_APPEND 2
20 JUMP_BACKWARD 10 (to 4)
22 RETURN_VALUE


0 BUILD_LIST 0
2 LOAD_FAST 0 (.0)
4 FOR_ITER 9 (to 22)
6 UNPACK_SEQUENCE 2
8 STORE_FAST 1 (field)
10 STORE_FAST 2 (success)
12 LOAD_FAST 2 (success)
14 POP_JUMP_BACKWARD_IF_FALSE 7 (to 4)
16 LOAD_FAST 1 (field)
18 LIST_APPEND 2
20 JUMP_BACKWARD 10 (to 4)
22 RETURN_VALUE

0 COPY_FREE_VARS 1

2 BUILD_LIST 0
4 LOAD_FAST 0 (.0)
6 FOR_ITER 26 (to 28)
8 STORE_FAST 1 (field)
10 LOAD_DEREF 2 (form_success)
12 LOAD_METHOD 0 (get)
14 LOAD_FAST 1 (field)
16 LOAD_CONST 0 (False)
18 CALL 2
20 POP_JUMP_BACKWARD_IF_TRUE 24 (to 6)
22 LOAD_FAST 1 (field)
24 LIST_APPEND 2
26 JUMP_BACKWARD 27 (to 6)
28 RETURN_VALUE


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("BIRTH_DATE")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_CONST 3 (0)
22 LOAD_CONST 4 (None)
24 IMPORT_NAME 2 (random)
26 STORE_FAST 1 (random)

28 LOAD_CONST 3 (0)
30 LOAD_CONST 5 (('datetime',))
32 IMPORT_NAME 3 (datetime)
34 IMPORT_FROM 3 (datetime)
36 STORE_FAST 2 (datetime)
38 POP_TOP

40 LOAD_FAST 2 (datetime)
42 LOAD_METHOD 4 (now)
44 CALL 0
46 LOAD_ATTR 5 (year)
48 STORE_FAST 3 (current_year)

50 LOAD_FAST 1 (random)
52 LOAD_METHOD 6 (randint)
54 LOAD_FAST 3 (current_year)
56 LOAD_CONST 6 (65)
58 BINARY_OP 10
60 LOAD_FAST 3 (current_year)
62 LOAD_CONST 7 (18)
64 BINARY_OP 10
66 CALL 2
68 STORE_FAST 4 (birth_year)

70 LOAD_FAST 1 (random)
72 LOAD_METHOD 6 (randint)
74 LOAD_CONST 8 (1)
76 LOAD_CONST 9 (12)
78 CALL 2
80 STORE_FAST 5 (birth_month)

82 LOAD_FAST 1 (random)
84 LOAD_METHOD 6 (randint)
86 LOAD_CONST 8 (1)
88 LOAD_CONST 10 (28)
90 CALL 2
92 STORE_FAST 6 (birth_day)

94 BUILD_LIST 0
96 LOAD_CONST 11 (('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))
98 LIST_EXTEND 1
100 STORE_FAST 7 (month_names)

102 LOAD_FAST 7 (month_names)
104 LOAD_FAST 5 (birth_month)
106 LOAD_CONST 8 (1)
108 BINARY_OP 10
110 BINARY_SUBSCR
112 STORE_FAST 8 (month_name)

114 BUILD_LIST 0
116 LOAD_CONST 12 (("select[name='dob_month']", "select[name='user[dob_month]']", "select[name='month']", "select[id*='month']"))
118 LIST_EXTEND 1
120 STORE_FAST 9 (month_selectors)

122 LOAD_FAST 9 (month_selectors)
124 GET_ITER
126 FOR_ITER 115 (to 242)
128 STORE_FAST 10 (selector)

130 NOP

132 LOAD_FAST 0 (self)
134 LOAD_ATTR 7 (page)
136 LOAD_METHOD 8 (query_selector)
138 LOAD_FAST 10 (selector)
140 CALL 1
142 GET_AWAITABLE 0
144 LOAD_CONST 4 (None)
146 SEND 3 (to 152)
148 YIELD_VALUE
150 JUMP_BACKWARD_NO_INTERRUPT 4 (to 146)
152 STORE_FAST 11 (element)

154 LOAD_FAST 11 (element)
156 POP_JUMP_FORWARD_IF_FALSE 55 (to 204)

158 LOAD_FAST 11 (element)
160 LOAD_METHOD 9 (select_option)
162 LOAD_FAST 8 (month_name)
164 KW_NAMES 13 (('label',))
166 CALL 1
168 GET_AWAITABLE 0
170 LOAD_CONST 4 (None)
172 SEND 3 (to 178)
174 YIELD_VALUE
176 JUMP_BACKWARD_NO_INTERRUPT 4 (to 172)
178 POP_TOP

180 LOAD_GLOBAL 1 (NULL + log_automation_step)
182 LOAD_FAST 0 (self)
184 LOAD_ATTR 1 (logger)
186 LOAD_CONST 14 ("BIRTH_MONTH")
188 LOAD_CONST 15 ("SUCCESS")
190 LOAD_CONST 16 ("month")
192 LOAD_FAST 8 (month_name)
194 BUILD_MAP 1
196 CALL 4
198 POP_TOP

200 POP_TOP
202 JUMP_FORWARD 24 (to 242)

204 JUMP_BACKWARD 93 (to 126)
206 PUSH_EXC_INFO

208 LOAD_GLOBAL 20 (Exception)
210 CHECK_EXC_MATCH
212 POP_JUMP_FORWARD_IF_FALSE 10 (to 234)
214 STORE_FAST 12 (e)

216 POP_EXCEPT
218 LOAD_CONST 4 (None)
220 STORE_FAST 12 (e)
222 DELETE_FAST 12 (e)
224 JUMP_BACKWARD 108 (to 126)
226 LOAD_CONST 4 (None)
228 STORE_FAST 12 (e)
230 DELETE_FAST 12 (e)
232 RERAISE 1

234 RERAISE 0
236 COPY 3
238 POP_EXCEPT
240 RERAISE 1

242 BUILD_LIST 0
244 LOAD_CONST 17 (("input[name='dob_day']", "input[name='user[dob_day]']", "input[name='day']", "input[id*='day']"))
246 LIST_EXTEND 1
248 STORE_FAST 13 (day_selectors)

250 LOAD_FAST 13 (day_selectors)
252 GET_ITER
254 FOR_ITER 127 (to 372)
256 STORE_FAST 10 (selector)

258 NOP

260 LOAD_FAST 0 (self)
262 LOAD_ATTR 7 (page)
264 LOAD_METHOD 8 (query_selector)
266 LOAD_FAST 10 (selector)
268 CALL 1
270 GET_AWAITABLE 0
272 LOAD_CONST 4 (None)
274 SEND 3 (to 280)
276 YIELD_VALUE
278 JUMP_BACKWARD_NO_INTERRUPT 4 (to 274)
280 STORE_FAST 11 (element)

282 LOAD_FAST 11 (element)
284 POP_JUMP_FORWARD_IF_FALSE 67 (to 334)

286 LOAD_FAST 11 (element)
288 LOAD_METHOD 11 (fill)
290 LOAD_GLOBAL 25 (NULL + str)
292 LOAD_FAST 6 (birth_day)
294 CALL 1
296 CALL 1
298 GET_AWAITABLE 0
300 LOAD_CONST 4 (None)
302 SEND 3 (to 308)
304 YIELD_VALUE
306 JUMP_BACKWARD_NO_INTERRUPT 4 (to 302)
308 POP_TOP

310 LOAD_GLOBAL 1 (NULL + log_automation_step)
312 LOAD_FAST 0 (self)
314 LOAD_ATTR 1 (logger)
316 LOAD_CONST 18 ("BIRTH_DAY")
318 LOAD_CONST 15 ("SUCCESS")
320 LOAD_CONST 19 ("day")
322 LOAD_FAST 6 (birth_day)
324 BUILD_MAP 1
326 CALL 4
328 POP_TOP

330 POP_TOP
332 JUMP_FORWARD 24 (to 372)

334 JUMP_BACKWARD 105 (to 254)
336 PUSH_EXC_INFO

338 LOAD_GLOBAL 20 (Exception)
340 CHECK_EXC_MATCH
342 POP_JUMP_FORWARD_IF_FALSE 10 (to 364)
344 STORE_FAST 12 (e)

346 POP_EXCEPT
348 LOAD_CONST 4 (None)
350 STORE_FAST 12 (e)
352 DELETE_FAST 12 (e)
354 JUMP_BACKWARD 120 (to 254)
356 LOAD_CONST 4 (None)
358 STORE_FAST 12 (e)
360 DELETE_FAST 12 (e)
362 RERAISE 1

364 RERAISE 0
366 COPY 3
368 POP_EXCEPT
370 RERAISE 1

372 BUILD_LIST 0
374 LOAD_CONST 20 (("input[name='dob_year']", "input[name='user[dob_year]']", "input[name='year']", "input[id*='year']"))
376 LIST_EXTEND 1
378 STORE_FAST 14 (year_selectors)

380 LOAD_FAST 14 (year_selectors)
382 GET_ITER
384 FOR_ITER 127 (to 502)
386 STORE_FAST 10 (selector)

388 NOP

390 LOAD_FAST 0 (self)
392 LOAD_ATTR 7 (page)
394 LOAD_METHOD 8 (query_selector)
396 LOAD_FAST 10 (selector)
398 CALL 1
400 GET_AWAITABLE 0
402 LOAD_CONST 4 (None)
404 SEND 3 (to 410)
406 YIELD_VALUE
408 JUMP_BACKWARD_NO_INTERRUPT 4 (to 404)
410 STORE_FAST 11 (element)

412 LOAD_FAST 11 (element)
414 POP_JUMP_FORWARD_IF_FALSE 67 (to 464)

416 LOAD_FAST 11 (element)
418 LOAD_METHOD 11 (fill)
420 LOAD_GLOBAL 25 (NULL + str)
422 LOAD_FAST 4 (birth_year)
424 CALL 1
426 CALL 1
428 GET_AWAITABLE 0
430 LOAD_CONST 4 (None)
432 SEND 3 (to 438)
434 YIELD_VALUE
436 JUMP_BACKWARD_NO_INTERRUPT 4 (to 432)
438 POP_TOP

440 LOAD_GLOBAL 1 (NULL + log_automation_step)
442 LOAD_FAST 0 (self)
444 LOAD_ATTR 1 (logger)
446 LOAD_CONST 21 ("BIRTH_YEAR")
448 LOAD_CONST 15 ("SUCCESS")
450 LOAD_CONST 22 ("year")
452 LOAD_FAST 4 (birth_year)
454 BUILD_MAP 1
456 CALL 4
458 POP_TOP

460 POP_TOP
462 JUMP_FORWARD 24 (to 502)

464 JUMP_BACKWARD 105 (to 384)
466 PUSH_EXC_INFO

468 LOAD_GLOBAL 20 (Exception)
470 CHECK_EXC_MATCH
472 POP_JUMP_FORWARD_IF_FALSE 10 (to 494)
474 STORE_FAST 12 (e)

476 POP_EXCEPT
478 LOAD_CONST 4 (None)
480 STORE_FAST 12 (e)
482 DELETE_FAST 12 (e)
484 JUMP_BACKWARD 120 (to 384)
486 LOAD_CONST 4 (None)
488 STORE_FAST 12 (e)
490 DELETE_FAST 12 (e)
492 RERAISE 1

494 RERAISE 0
496 COPY 3
498 POP_EXCEPT
500 RERAISE 1

502 LOAD_GLOBAL 1 (NULL + log_automation_step)
504 LOAD_FAST 0 (self)
506 LOAD_ATTR 1 (logger)
508 LOAD_CONST 1 ("BIRTH_DATE")
510 LOAD_CONST 15 ("SUCCESS")
512 CALL 3
514 POP_TOP
516 LOAD_CONST 4 (None)
518 RETURN_VALUE
520 PUSH_EXC_INFO

522 LOAD_GLOBAL 20 (Exception)
524 CHECK_EXC_MATCH
526 POP_JUMP_FORWARD_IF_FALSE 49 (to 574)
528 STORE_FAST 12 (e)

530 LOAD_GLOBAL 1 (NULL + log_automation_step)
532 LOAD_FAST 0 (self)
534 LOAD_ATTR 1 (logger)
536 LOAD_CONST 1 ("BIRTH_DATE")
538 LOAD_CONST 23 ("ERROR")
540 LOAD_CONST 24 ("error")
542 LOAD_GLOBAL 25 (NULL + str)
544 LOAD_FAST 12 (e)
546 CALL 1
548 BUILD_MAP 1
550 CALL 4
552 POP_TOP
554 POP_EXCEPT
556 LOAD_CONST 4 (None)
558 STORE_FAST 12 (e)
560 DELETE_FAST 12 (e)
562 LOAD_CONST 4 (None)
564 RETURN_VALUE
566 LOAD_CONST 4 (None)
568 STORE_FAST 12 (e)
570 DELETE_FAST 12 (e)
572 RERAISE 1

574 RERAISE 0
576 COPY 3
578 POP_EXCEPT
580 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("NEWSLETTER_CHECKBOX")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 BUILD_LIST 0
22 LOAD_CONST 3 (("input[type='checkbox'][name*='updates']", "input[type='checkbox'][name*='newsletter']", "input[type='checkbox'][name*='marketing']", "input[type='checkbox']:visible"))
24 LIST_EXTEND 1
26 STORE_FAST 1 (checkbox_selectors)

28 LOAD_FAST 1 (checkbox_selectors)
30 GET_ITER
32 FOR_ITER 168 (to 190)
34 STORE_FAST 2 (selector)

36 NOP

38 LOAD_FAST 0 (self)
40 LOAD_ATTR 2 (page)
42 LOAD_METHOD 3 (query_selector)
44 LOAD_FAST 2 (selector)
46 CALL 1
48 GET_AWAITABLE 0
50 LOAD_CONST 4 (None)
52 SEND 3 (to 58)
54 YIELD_VALUE
56 JUMP_BACKWARD_NO_INTERRUPT 4 (to 52)
58 STORE_FAST 3 (element)

60 LOAD_FAST 3 (element)
62 POP_JUMP_FORWARD_IF_FALSE 108 (to 152)

64 LOAD_FAST 3 (element)
66 LOAD_METHOD 4 (is_checked)
68 CALL 0
70 GET_AWAITABLE 0
72 LOAD_CONST 4 (None)
74 SEND 3 (to 80)
76 YIELD_VALUE
78 JUMP_BACKWARD_NO_INTERRUPT 4 (to 74)
80 STORE_FAST 4 (is_checked)

82 LOAD_FAST 4 (is_checked)
84 POP_JUMP_FORWARD_IF_TRUE 52 (to 126)

86 LOAD_FAST 3 (element)
88 LOAD_METHOD 5 (check)
90 CALL 0
92 GET_AWAITABLE 0
94 LOAD_CONST 4 (None)
96 SEND 3 (to 102)
98 YIELD_VALUE
100 JUMP_BACKWARD_NO_INTERRUPT 4 (to 96)
102 POP_TOP

104 LOAD_GLOBAL 1 (NULL + log_automation_step)
106 LOAD_FAST 0 (self)
108 LOAD_ATTR 1 (logger)
110 LOAD_CONST 1 ("NEWSLETTER_CHECKBOX")
112 LOAD_CONST 5 ("SUCCESS")
114 LOAD_CONST 6 ("action")
116 LOAD_CONST 7 ("checked")
118 BUILD_MAP 1
120 CALL 4
122 POP_TOP
124 JUMP_FORWARD 25 (to 146)

126 LOAD_GLOBAL 1 (NULL + log_automation_step)
128 LOAD_FAST 0 (self)
130 LOAD_ATTR 1 (logger)
132 LOAD_CONST 1 ("NEWSLETTER_CHECKBOX")
134 LOAD_CONST 5 ("SUCCESS")
136 LOAD_CONST 6 ("action")
138 LOAD_CONST 8 ("already_checked")
140 BUILD_MAP 1
142 CALL 4
144 POP_TOP

146 POP_TOP
148 LOAD_CONST 4 (None)
150 RETURN_VALUE

152 JUMP_BACKWARD 146 (to 32)
154 PUSH_EXC_INFO

156 LOAD_GLOBAL 12 (Exception)
158 CHECK_EXC_MATCH
160 POP_JUMP_FORWARD_IF_FALSE 10 (to 182)
162 STORE_FAST 5 (e)

164 POP_EXCEPT
166 LOAD_CONST 4 (None)
168 STORE_FAST 5 (e)
170 DELETE_FAST 5 (e)
172 JUMP_BACKWARD 161 (to 32)
174 LOAD_CONST 4 (None)
176 STORE_FAST 5 (e)
178 DELETE_FAST 5 (e)
180 RERAISE 1

182 RERAISE 0
184 COPY 3
186 POP_EXCEPT
188 RERAISE 1

190 LOAD_CONST 4 (None)
192 RETURN_VALUE
194 PUSH_EXC_INFO

196 LOAD_GLOBAL 12 (Exception)
198 CHECK_EXC_MATCH
200 POP_JUMP_FORWARD_IF_FALSE 49 (to 248)
202 STORE_FAST 5 (e)

204 LOAD_GLOBAL 1 (NULL + log_automation_step)
206 LOAD_FAST 0 (self)
208 LOAD_ATTR 1 (logger)
210 LOAD_CONST 1 ("NEWSLETTER_CHECKBOX")
212 LOAD_CONST 9 ("ERROR")
214 LOAD_CONST 10 ("error")
216 LOAD_GLOBAL 15 (NULL + str)
218 LOAD_FAST 5 (e)
220 CALL 1
222 BUILD_MAP 1
224 CALL 4
226 POP_TOP
228 POP_EXCEPT
230 LOAD_CONST 4 (None)
232 STORE_FAST 5 (e)
234 DELETE_FAST 5 (e)
236 LOAD_CONST 4 (None)
238 RETURN_VALUE
240 LOAD_CONST 4 (None)
242 STORE_FAST 5 (e)
244 DELETE_FAST 5 (e)
246 RERAISE 1

248 RERAISE 0
250 COPY 3
252 POP_EXCEPT
254 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_CONST 1 (None)
6 STORE_FAST 1 (anchor_frame)

8 LOAD_CONST 1 (None)
10 STORE_FAST 2 (challenge_frame)

12 NOP

14 LOAD_FAST 0 (self)
16 LOAD_ATTR 0 (page)
18 LOAD_ATTR 1 (frames)
20 GET_ITER
22 FOR_ITER 49 (to 82)
24 STORE_FAST 3 (fr)

26 LOAD_FAST 3 (fr)
28 LOAD_ATTR 2 (url)
30 JUMP_IF_TRUE_OR_POP 1 (to 34)
32 LOAD_CONST 2 ("")
34 LOAD_METHOD 3 (lower)
36 CALL 0
38 STORE_FAST 4 (url)

40 LOAD_CONST 3 ("api2/anchor")
42 LOAD_FAST 4 (url)
44 CONTAINS_OP 0 (in)
46 POP_JUMP_FORWARD_IF_TRUE 4 (to 56)
48 LOAD_CONST 4 ("enterprise/anchor")
50 LOAD_FAST 4 (url)
52 CONTAINS_OP 0 (in)
54 POP_JUMP_FORWARD_IF_FALSE 2 (to 60)

56 LOAD_FAST 3 (fr)
58 STORE_FAST 1 (anchor_frame)

60 LOAD_CONST 5 ("api2/bframe")
62 LOAD_FAST 4 (url)
64 CONTAINS_OP 0 (in)
66 POP_JUMP_FORWARD_IF_TRUE 4 (to 76)
68 LOAD_CONST 6 ("enterprise/bframe")
70 LOAD_FAST 4 (url)
72 CONTAINS_OP 0 (in)
74 POP_JUMP_FORWARD_IF_FALSE 2 (to 80)

76 LOAD_FAST 3 (fr)
78 STORE_FAST 2 (challenge_frame)
80 JUMP_BACKWARD 50 (to 22)

82 JUMP_FORWARD 16 (to 106)
84 PUSH_EXC_INFO

86 LOAD_GLOBAL 8 (Exception)
88 CHECK_EXC_MATCH
90 POP_JUMP_FORWARD_IF_FALSE 3 (to 98)
92 POP_TOP

94 POP_EXCEPT
96 JUMP_FORWARD 4 (to 106)

98 RERAISE 0
100 COPY 3
102 POP_EXCEPT
104 RERAISE 1

106 LOAD_FAST 1 (anchor_frame)
108 LOAD_FAST 2 (challenge_frame)
110 BUILD_TUPLE 2
112 RETURN_VALUE


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_CONST 1 ('\n            async (opts) => {\n              const maxSteps = (opts && opts.maxSteps) || 20;\n              const fast = !!(opts && opts.fast);\n              const sel = "iframe[src*=\'api2/anchor\'], iframe[src*=\'enterprise/anchor\'], .g-recaptcha, [data-sitekey]";\n              const exists = () => !!document.querySelector(sel);\n              const center = () => {\n                try {\n                  const t = document.querySelector(sel);\n                  t?.scrollIntoView({block:\'center\', inline:\'center\'});\n                } catch(_){}\n              };\n              // Jika frame anchor sudah ada, anggap captcha sudah render\n              try {\n                const frs = Array.from(window.top.frames || []);\n                for (const fr of frs) {\n                  try {\n                    const u = (fr.location?.href || \'\').toLowerCase();\n                    if (u.includes(\'api2/anchor\') || u.includes(\'enterprise/anchor\')) { return true; }\n                  } catch(_){}\n                }\n              } catch(_){}\n              if (exists()) { center(); return true; }\n              const uniq = (arr) => Array.from(new Set(arr.filter(Boolean)));\n              const getScrollable = () => {\n                const list = [];\n                try { list.push(document.scrollingElement || document.documentElement || document.body); } catch(_){}\n                const cand = Array.from(document.querySelectorAll(\'main, [role="main"], form, .container, [class*="container"], [class*="content"], [style*="overflow"], body\'));\n                for (const el of cand) {\n                  try {\n                    const cs = getComputedStyle(el);\n                    const can = (el.scrollHeight > (el.clientHeight||0)+10) && /(auto|scroll)/i.test(cs.overflowY || cs.overflow || \'\');\n                    if (can) list.push(el);\n                  } catch(_){}\n                }\n                return uniq(list);\n              };\n              const scrollers = getScrollable();\n              // Fast path: langsung ke bawah dulu\n              if (fast) {\n                try {\n                  for (const el of scrollers){\n                    try {\n                      if (el === document.body || el === document.documentElement){\n                        window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight || 999999);\n                      } else {\n                        el.scrollTop = el.scrollHeight;\n                      }\n                    } catch(_){}}\n                  await new Promise(r=>setTimeout(r, 30));\n                  if (exists()) { center(); return true; }\n                } catch(_){}}\n              for (let i=0; i<Math.max(1, maxSteps||20); i++){\n                for (const el of scrollers){\n                  try {\n                    if (el === document.body || el === document.documentElement){\n                      window.scrollBy(0, Math.round((window.innerHeight||600)*0.9));\n                    } else if (el.scrollBy){\n                      el.scrollBy(0, Math.round((el.clientHeight||400)*0.9));\n                    } else {\n                      el.scrollTop = Math.min(el.scrollTop + Math.round((el.clientHeight||400)*0.9), el.scrollHeight);\n                    }\n                  } catch(_){}\n                }\n                await new Promise(r=>setTimeout(r, 180));\n                if (exists()) { center(); return true; }\n              }\n              // Paksa ke bawah\n              for (const el of scrollers){ try { el.scrollTop = el.scrollHeight; } catch(_){} }\n              await new Promise(r=>setTimeout(r, 200));\n              if (exists()) { center(); return true; }\n              return false;\n            }\n            ')
8 STORE_FAST 4 (js)

10 LOAD_FAST 0 (self)
12 LOAD_ATTR 0 (page)
14 LOAD_METHOD 1 (evaluate)
16 LOAD_FAST 4 (js)
18 LOAD_FAST 1 (max_steps)
20 LOAD_FAST 2 (fast)
22 LOAD_CONST 2 (('maxSteps', 'fast'))
24 BUILD_CONST_KEY_MAP 2
26 CALL 2
28 GET_AWAITABLE 0
30 LOAD_CONST 3 (None)
32 SEND 3 (to 38)
34 YIELD_VALUE
36 JUMP_BACKWARD_NO_INTERRUPT 4 (to 32)
38 STORE_FAST 5 (ok)

40 LOAD_FAST 5 (ok)
42 POP_JUMP_FORWARD_IF_FALSE 23 (to 60)

44 LOAD_GLOBAL 5 (NULL + log_automation_step)
46 LOAD_FAST 0 (self)
48 LOAD_ATTR 3 (logger)
50 LOAD_CONST 4 ("CAPTCHA_SCROLL")
52 LOAD_CONST 5 ("FOUND")
54 CALL 3
56 POP_TOP
58 JUMP_FORWARD 22 (to 74)

60 LOAD_GLOBAL 5 (NULL + log_automation_step)
62 LOAD_FAST 0 (self)
64 LOAD_ATTR 3 (logger)
66 LOAD_CONST 4 ("CAPTCHA_SCROLL")
68 LOAD_CONST 6 ("NOT_FOUND")
70 CALL 3
72 POP_TOP

74 LOAD_FAST 5 (ok)
76 POP_JUMP_FORWARD_IF_FALSE 2 (to 82)

78 LOAD_CONST 7 (True)
80 RETURN_VALUE

82 LOAD_FAST 3 (skip_fallback)
84 POP_JUMP_FORWARD_IF_FALSE 2 (to 90)

86 LOAD_CONST 8 (False)
88 RETURN_VALUE

90 NOP

92 NOP

94 LOAD_FAST 0 (self)
96 LOAD_ATTR 0 (page)
98 LOAD_METHOD 1 (evaluate)
100 LOAD_CONST 9 ("try{document.activeElement && document.activeElement.blur()}catch(e){}")
102 CALL 1
104 GET_AWAITABLE 0
106 LOAD_CONST 3 (None)
108 SEND 3 (to 114)
110 YIELD_VALUE
112 JUMP_BACKWARD_NO_INTERRUPT 4 (to 108)
114 POP_TOP
116 JUMP_FORWARD 16 (to 140)
118 PUSH_EXC_INFO

120 LOAD_GLOBAL 8 (Exception)
122 CHECK_EXC_MATCH
124 POP_JUMP_FORWARD_IF_FALSE 3 (to 132)
126 POP_TOP

128 POP_EXCEPT
130 JUMP_FORWARD 4 (to 140)

132 RERAISE 0
134 COPY 3
136 POP_EXCEPT
138 RERAISE 1

140 LOAD_CONST 10 ("iframe[src*='api2/anchor'], iframe[src*='enterprise/anchor'], .g-recaptcha, [data-sitekey]")
142 STORE_FAST 6 (sel)

144 LOAD_GLOBAL 11 (NULL + range)
146 LOAD_CONST 11 (12)
148 CALL 1
150 GET_ITER
152 FOR_ITER 168 (to 292)
154 STORE_FAST 7 (_)

156 LOAD_FAST 0 (self)
158 LOAD_ATTR 0 (page)
160 LOAD_ATTR 6 (keyboard)
162 LOAD_METHOD 7 (press)
164 LOAD_CONST 12 ("PageDown")
166 CALL 1
168 GET_AWAITABLE 0
170 LOAD_CONST 3 (None)
172 SEND 3 (to 178)
174 YIELD_VALUE
176 JUMP_BACKWARD_NO_INTERRUPT 4 (to 172)
178 POP_TOP

180 LOAD_GLOBAL 17 (NULL + asyncio)
182 LOAD_ATTR 9 (sleep)
184 LOAD_CONST 13 (0.15)
186 CALL 1
188 GET_AWAITABLE 0
190 LOAD_CONST 3 (None)
192 SEND 3 (to 198)
194 YIELD_VALUE
196 JUMP_BACKWARD_NO_INTERRUPT 4 (to 192)
198 POP_TOP

200 LOAD_FAST 0 (self)
202 LOAD_ATTR 0 (page)
204 LOAD_METHOD 10 (query_selector)
206 LOAD_FAST 6 (sel)
208 CALL 1
210 GET_AWAITABLE 0
212 LOAD_CONST 3 (None)
214 SEND 3 (to 220)
216 YIELD_VALUE
218 JUMP_BACKWARD_NO_INTERRUPT 4 (to 214)
220 STORE_FAST 8 (el)

222 LOAD_FAST 8 (el)
224 POP_JUMP_FORWARD_IF_FALSE 69 (to 290)

226 NOP

228 LOAD_FAST 8 (el)
230 LOAD_METHOD 11 (scroll_into_view_if_needed)
232 CALL 0
234 GET_AWAITABLE 0
236 LOAD_CONST 3 (None)
238 SEND 3 (to 244)
240 YIELD_VALUE
242 JUMP_BACKWARD_NO_INTERRUPT 4 (to 238)
244 POP_TOP
246 JUMP_FORWARD 16 (to 270)
248 PUSH_EXC_INFO

250 LOAD_GLOBAL 8 (Exception)
252 CHECK_EXC_MATCH
254 POP_JUMP_FORWARD_IF_FALSE 3 (to 262)
256 POP_TOP

258 POP_EXCEPT
260 JUMP_FORWARD 4 (to 270)

262 RERAISE 0
264 COPY 3
266 POP_EXCEPT
268 RERAISE 1

270 LOAD_GLOBAL 5 (NULL + log_automation_step)
272 LOAD_FAST 0 (self)
274 LOAD_ATTR 3 (logger)
276 LOAD_CONST 4 ("CAPTCHA_SCROLL")
278 LOAD_CONST 14 ("FOUND_AFTER_PAGEDOWN")
280 CALL 3
282 POP_TOP

284 POP_TOP
286 LOAD_CONST 7 (True)
288 RETURN_VALUE

290 JUMP_BACKWARD 169 (to 152)

292 NOP

294 LOAD_FAST 0 (self)
296 LOAD_ATTR 0 (page)
298 LOAD_ATTR 6 (keyboard)
300 LOAD_METHOD 7 (press)
302 LOAD_CONST 15 ("End")
304 CALL 1
306 GET_AWAITABLE 0
308 LOAD_CONST 3 (None)
310 SEND 3 (to 316)
312 YIELD_VALUE
314 JUMP_BACKWARD_NO_INTERRUPT 4 (to 310)
316 POP_TOP
318 JUMP_FORWARD 16 (to 342)
320 PUSH_EXC_INFO

322 LOAD_GLOBAL 8 (Exception)
324 CHECK_EXC_MATCH
326 POP_JUMP_FORWARD_IF_FALSE 3 (to 334)
328 POP_TOP

330 POP_EXCEPT
332 JUMP_FORWARD 4 (to 342)

334 RERAISE 0
336 COPY 3
338 POP_EXCEPT
340 RERAISE 1

342 LOAD_GLOBAL 17 (NULL + asyncio)
344 LOAD_ATTR 9 (sleep)
346 LOAD_CONST 16 (0.2)
348 CALL 1
350 GET_AWAITABLE 0
352 LOAD_CONST 3 (None)
354 SEND 3 (to 360)
356 YIELD_VALUE
358 JUMP_BACKWARD_NO_INTERRUPT 4 (to 354)
360 POP_TOP

362 LOAD_FAST 0 (self)
364 LOAD_ATTR 0 (page)
366 LOAD_METHOD 10 (query_selector)
368 LOAD_FAST 6 (sel)
370 CALL 1
372 GET_AWAITABLE 0
374 LOAD_CONST 3 (None)
376 SEND 3 (to 382)
378 YIELD_VALUE
380 JUMP_BACKWARD_NO_INTERRUPT 4 (to 376)
382 STORE_FAST 8 (el)

384 LOAD_FAST 8 (el)
386 POP_JUMP_FORWARD_IF_FALSE 68 (to 450)

388 NOP

390 LOAD_FAST 8 (el)
392 LOAD_METHOD 11 (scroll_into_view_if_needed)
394 CALL 0
396 GET_AWAITABLE 0
398 LOAD_CONST 3 (None)
400 SEND 3 (to 406)
402 YIELD_VALUE
404 JUMP_BACKWARD_NO_INTERRUPT 4 (to 400)
406 POP_TOP
408 JUMP_FORWARD 16 (to 432)
410 PUSH_EXC_INFO

412 LOAD_GLOBAL 8 (Exception)
414 CHECK_EXC_MATCH
416 POP_JUMP_FORWARD_IF_FALSE 3 (to 424)
418 POP_TOP

420 POP_EXCEPT
422 JUMP_FORWARD 4 (to 432)

424 RERAISE 0
426 COPY 3
428 POP_EXCEPT
430 RERAISE 1

432 LOAD_GLOBAL 5 (NULL + log_automation_step)
434 LOAD_FAST 0 (self)
436 LOAD_ATTR 3 (logger)
438 LOAD_CONST 4 ("CAPTCHA_SCROLL")
440 LOAD_CONST 17 ("FOUND_AFTER_END")
442 CALL 3
444 POP_TOP

446 LOAD_CONST 7 (True)
448 RETURN_VALUE

450 JUMP_FORWARD 16 (to 474)
452 PUSH_EXC_INFO

454 LOAD_GLOBAL 8 (Exception)
456 CHECK_EXC_MATCH
458 POP_JUMP_FORWARD_IF_FALSE 3 (to 466)
460 POP_TOP

462 POP_EXCEPT
464 JUMP_FORWARD 4 (to 474)

466 RERAISE 0
468 COPY 3
470 POP_EXCEPT
472 RERAISE 1

474 LOAD_CONST 8 (False)
476 RETURN_VALUE
478 PUSH_EXC_INFO

480 LOAD_GLOBAL 8 (Exception)
482 CHECK_EXC_MATCH
484 POP_JUMP_FORWARD_IF_FALSE 49 (to 532)
486 STORE_FAST 9 (e)

488 LOAD_GLOBAL 5 (NULL + log_automation_step)
490 LOAD_FAST 0 (self)
492 LOAD_ATTR 3 (logger)
494 LOAD_CONST 4 ("CAPTCHA_SCROLL")
496 LOAD_CONST 18 ("ERROR")
498 LOAD_CONST 19 ("error")
500 LOAD_GLOBAL 25 (NULL + str)
502 LOAD_FAST 9 (e)
504 CALL 1
506 BUILD_MAP 1
508 CALL 4
510 POP_TOP

512 POP_EXCEPT
514 LOAD_CONST 3 (None)
516 STORE_FAST 9 (e)
518 DELETE_FAST 9 (e)
520 LOAD_CONST 8 (False)
522 RETURN_VALUE
524 LOAD_CONST 3 (None)
526 STORE_FAST 9 (e)
528 DELETE_FAST 9 (e)
530 RERAISE 1

532 RERAISE 0
534 COPY 3
536 POP_EXCEPT
538 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 NOP

8 LOAD_FAST 0 (self)
10 LOAD_METHOD 0 (_scroll_to_recaptcha)
12 LOAD_CONST 1 (5)
14 LOAD_CONST 2 (True)
16 LOAD_CONST 2 (True)
18 KW_NAMES 3 (('max_steps', 'fast', 'skip_fallback'))
20 CALL 3
22 GET_AWAITABLE 0
24 LOAD_CONST 4 (None)
26 SEND 3 (to 32)
28 YIELD_VALUE
30 JUMP_BACKWARD_NO_INTERRUPT 4 (to 26)
32 POP_TOP
34 JUMP_FORWARD 16 (to 58)
36 PUSH_EXC_INFO

38 LOAD_GLOBAL 2 (Exception)
40 CHECK_EXC_MATCH
42 POP_JUMP_FORWARD_IF_FALSE 3 (to 50)
44 POP_TOP

46 POP_EXCEPT
48 JUMP_FORWARD 4 (to 58)

50 RERAISE 0
52 COPY 3
54 POP_EXCEPT
56 RERAISE 1

58 LOAD_CONST 4 (None)
60 STORE_FAST 1 (anchor_frame)

62 LOAD_CONST 4 (None)
64 STORE_FAST 2 (_challenge)

66 LOAD_GLOBAL 5 (NULL + range)
68 LOAD_CONST 5 (3)
70 CALL 1
72 GET_ITER
74 FOR_ITER 61 (to 130)
76 STORE_FAST 3 (_)

78 LOAD_FAST 0 (self)
80 LOAD_METHOD 3 (_find_recaptcha_frames)
82 CALL 0
84 GET_AWAITABLE 0
86 LOAD_CONST 4 (None)
88 SEND 3 (to 94)
90 YIELD_VALUE
92 JUMP_BACKWARD_NO_INTERRUPT 4 (to 88)
94 UNPACK_SEQUENCE 2
96 STORE_FAST 1 (anchor_frame)
98 STORE_FAST 2 (_challenge)

100 LOAD_FAST 1 (anchor_frame)
102 POP_JUMP_FORWARD_IF_FALSE 2 (to 108)

104 POP_TOP
106 JUMP_FORWARD 27 (to 130)

108 LOAD_GLOBAL 9 (NULL + asyncio)
110 LOAD_ATTR 5 (sleep)
112 LOAD_CONST 6 (0.05)
114 CALL 1
116 GET_AWAITABLE 0
118 LOAD_CONST 4 (None)
120 SEND 3 (to 126)
122 YIELD_VALUE
124 JUMP_BACKWARD_NO_INTERRUPT 4 (to 120)
126 POP_TOP
128 JUMP_BACKWARD 62 (to 74)

130 LOAD_FAST 1 (anchor_frame)
132 JUMP_IF_TRUE_OR_POP 6 (to 138)
134 LOAD_FAST 0 (self)
136 LOAD_ATTR 6 (page)
138 STORE_FAST 4 (target)

140 LOAD_CONST 7 ("#recaptcha-anchor")

142 LOAD_CONST 8 ("div[role='checkbox'][aria-checked='false']")
144 BUILD_LIST 2
146 STORE_FAST 5 (sel_candidates)

148 LOAD_FAST 5 (sel_candidates)
150 GET_ITER
152 FOR_ITER 291 (to 430)
154 STORE_FAST 6 (sel)

156 NOP

158 LOAD_FAST 4 (target)
160 LOAD_METHOD 7 (query_selector)
162 LOAD_FAST 6 (sel)
164 CALL 1
166 GET_AWAITABLE 0
168 LOAD_CONST 4 (None)
170 SEND 3 (to 176)
172 YIELD_VALUE
174 JUMP_BACKWARD_NO_INTERRUPT 4 (to 170)
176 STORE_FAST 7 (el)
178 JUMP_FORWARD 18 (to 206)
180 PUSH_EXC_INFO

182 LOAD_GLOBAL 2 (Exception)
184 CHECK_EXC_MATCH
186 POP_JUMP_FORWARD_IF_FALSE 5 (to 198)
188 POP_TOP

190 LOAD_CONST 4 (None)
192 STORE_FAST 7 (el)
194 POP_EXCEPT
196 JUMP_FORWARD 4 (to 206)

198 RERAISE 0
200 COPY 3
202 POP_EXCEPT
204 RERAISE 1

206 LOAD_FAST 7 (el)
208 POP_JUMP_FORWARD_IF_TRUE 1 (to 212)

210 JUMP_BACKWARD 53 (to 152)

212 NOP

214 LOAD_FAST 7 (el)
216 LOAD_METHOD 8 (scroll_into_view_if_needed)
218 CALL 0
220 GET_AWAITABLE 0
222 LOAD_CONST 4 (None)
224 SEND 3 (to 230)
226 YIELD_VALUE
228 JUMP_BACKWARD_NO_INTERRUPT 4 (to 224)
230 POP_TOP

232 LOAD_GLOBAL 9 (NULL + asyncio)
234 LOAD_ATTR 5 (sleep)
236 LOAD_CONST 9 (0.6)
238 CALL 1
240 GET_AWAITABLE 0
242 LOAD_CONST 4 (None)
244 SEND 3 (to 250)
246 YIELD_VALUE
248 JUMP_BACKWARD_NO_INTERRUPT 4 (to 244)
250 POP_TOP
252 JUMP_FORWARD 16 (to 276)
254 PUSH_EXC_INFO

256 LOAD_GLOBAL 2 (Exception)
258 CHECK_EXC_MATCH
260 POP_JUMP_FORWARD_IF_FALSE 3 (to 268)
262 POP_TOP

264 POP_EXCEPT
266 JUMP_FORWARD 4 (to 276)

268 RERAISE 0
270 COPY 3
272 POP_EXCEPT
274 RERAISE 1

276 NOP

278 LOAD_FAST 7 (el)
280 LOAD_METHOD 9 (click)
282 CALL 0
284 GET_AWAITABLE 0
286 LOAD_CONST 4 (None)
288 SEND 3 (to 294)
290 YIELD_VALUE
292 JUMP_BACKWARD_NO_INTERRUPT 4 (to 288)
294 POP_TOP
296 JUMP_FORWARD 63 (to 370)
298 PUSH_EXC_INFO

300 LOAD_GLOBAL 2 (Exception)
302 CHECK_EXC_MATCH
304 POP_JUMP_FORWARD_IF_FALSE 50 (to 362)
306 POP_TOP

308 NOP

310 LOAD_FAST 4 (target)
312 LOAD_METHOD 10 (evaluate)
314 LOAD_CONST 10 ("e => e.click()")
316 LOAD_FAST 7 (el)
318 CALL 2
320 GET_AWAITABLE 0
322 LOAD_CONST 4 (None)
324 SEND 3 (to 330)
326 YIELD_VALUE
328 JUMP_BACKWARD_NO_INTERRUPT 4 (to 324)
330 POP_TOP
332 JUMP_FORWARD 17 (to 358)
334 PUSH_EXC_INFO

336 LOAD_GLOBAL 2 (Exception)
338 CHECK_EXC_MATCH
340 POP_JUMP_FORWARD_IF_FALSE 4 (to 350)
342 POP_TOP

344 POP_EXCEPT
346 POP_EXCEPT
348 JUMP_BACKWARD 204 (to 152)

350 RERAISE 0
352 COPY 3
354 POP_EXCEPT
356 RERAISE 1

358 POP_EXCEPT
360 JUMP_FORWARD 4 (to 370)

362 RERAISE 0
364 COPY 3
366 POP_EXCEPT
368 RERAISE 1

370 LOAD_GLOBAL 9 (NULL + asyncio)
372 LOAD_ATTR 5 (sleep)
374 LOAD_CONST 11 (0.2)
376 CALL 1
378 GET_AWAITABLE 0
380 LOAD_CONST 4 (None)
382 SEND 3 (to 388)
384 YIELD_VALUE
386 JUMP_BACKWARD_NO_INTERRUPT 4 (to 382)
388 POP_TOP

390 LOAD_FAST 0 (self)
392 LOAD_METHOD 11 (_is_captcha_solved)
394 CALL 0
396 GET_AWAITABLE 0
398 LOAD_CONST 4 (None)
400 SEND 3 (to 406)
402 YIELD_VALUE
404 JUMP_BACKWARD_NO_INTERRUPT 4 (to 400)
406 POP_JUMP_FORWARD_IF_FALSE 25 (to 428)

408 LOAD_GLOBAL 25 (NULL + log_automation_step)
410 LOAD_FAST 0 (self)
412 LOAD_ATTR 13 (logger)
414 LOAD_CONST 12 ("CAPTCHA_CHECK")
416 LOAD_CONST 13 ("CHECKBOX_CLICKED")
418 CALL 3
420 POP_TOP

422 POP_TOP
424 LOAD_CONST 2 (True)
426 RETURN_VALUE

428 JUMP_BACKWARD 293 (to 152)

430 LOAD_CONST 14 (False)
432 RETURN_VALUE
434 PUSH_EXC_INFO

436 LOAD_GLOBAL 2 (Exception)
438 CHECK_EXC_MATCH
440 POP_JUMP_FORWARD_IF_FALSE 49 (to 488)
442 STORE_FAST 8 (e)

444 LOAD_GLOBAL 25 (NULL + log_automation_step)
446 LOAD_FAST 0 (self)
448 LOAD_ATTR 13 (logger)
450 LOAD_CONST 12 ("CAPTCHA_CHECK")
452 LOAD_CONST 15 ("CHECKBOX_CLICK_ERROR")
454 LOAD_CONST 16 ("error")
456 LOAD_GLOBAL 29 (NULL + str)
458 LOAD_FAST 8 (e)
460 CALL 1
462 BUILD_MAP 1
464 CALL 4
466 POP_TOP

468 POP_EXCEPT
470 LOAD_CONST 4 (None)
472 STORE_FAST 8 (e)
474 DELETE_FAST 8 (e)
476 LOAD_CONST 14 (False)
478 RETURN_VALUE
480 LOAD_CONST 4 (None)
482 STORE_FAST 8 (e)
484 DELETE_FAST 8 (e)
486 RERAISE 1

488 RERAISE 0
490 COPY 3
492 POP_EXCEPT
494 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("CAPTCHA_CHECK")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 NOP

22 LOAD_FAST 0 (self)
24 LOAD_METHOD 2 (_scroll_to_recaptcha)
26 LOAD_CONST 3 (5)
28 LOAD_CONST 4 (True)
30 LOAD_CONST 4 (True)
32 KW_NAMES 5 (('max_steps', 'fast', 'skip_fallback'))
34 CALL 3
36 GET_AWAITABLE 0
38 LOAD_CONST 6 (None)
40 SEND 3 (to 46)
42 YIELD_VALUE
44 JUMP_BACKWARD_NO_INTERRUPT 4 (to 40)
46 POP_TOP
48 JUMP_FORWARD 16 (to 72)
50 PUSH_EXC_INFO

52 LOAD_GLOBAL 6 (Exception)
54 CHECK_EXC_MATCH
56 POP_JUMP_FORWARD_IF_FALSE 3 (to 64)
58 POP_TOP

60 POP_EXCEPT
62 JUMP_FORWARD 4 (to 72)

64 RERAISE 0
66 COPY 3
68 POP_EXCEPT
70 RERAISE 1

72 BUILD_LIST 0
74 LOAD_CONST 7 (("iframe[title*='reCAPTCHA']", "iframe[src*='recaptcha']", '.g-recaptcha', '[data-sitekey]', '.captcha', '.h-captcha'))
76 LIST_EXTEND 1
78 STORE_FAST 1 (captcha_selectors)

80 LOAD_CONST 8 (False)
82 STORE_FAST 2 (captcha_found)

84 LOAD_FAST 1 (captcha_selectors)
86 GET_ITER
88 FOR_ITER 63 (to 144)
90 STORE_FAST 3 (selector)

92 LOAD_FAST 0 (self)
94 LOAD_ATTR 4 (page)
96 LOAD_METHOD 5 (query_selector)
98 LOAD_FAST 3 (selector)
100 CALL 1
102 GET_AWAITABLE 0
104 LOAD_CONST 6 (None)
106 SEND 3 (to 112)
108 YIELD_VALUE
110 JUMP_BACKWARD_NO_INTERRUPT 4 (to 106)
112 POP_JUMP_FORWARD_IF_FALSE 29 (to 142)

114 LOAD_CONST 4 (True)
116 STORE_FAST 2 (captcha_found)

118 LOAD_GLOBAL 1 (NULL + log_automation_step)
120 LOAD_FAST 0 (self)
122 LOAD_ATTR 1 (logger)
124 LOAD_CONST 9 ("CAPTCHA_DETECTED")
126 LOAD_CONST 10 ("FOUND")
128 LOAD_CONST 11 ("selector")
130 LOAD_FAST 3 (selector)
132 BUILD_MAP 1
134 CALL 4
136 POP_TOP

138 POP_TOP
140 JUMP_FORWARD 1 (to 144)

142 JUMP_BACKWARD 64 (to 88)

144 LOAD_FAST 2 (captcha_found)
146 POP_JUMP_FORWARD_IF_TRUE 24 (to 166)

148 LOAD_GLOBAL 1 (NULL + log_automation_step)
150 LOAD_FAST 0 (self)
152 LOAD_ATTR 1 (logger)
154 LOAD_CONST 1 ("CAPTCHA_CHECK")
156 LOAD_CONST 12 ("NOT_FOUND_AFTER_SCROLL")
158 CALL 3
160 POP_TOP

162 LOAD_CONST 4 (True)
164 RETURN_VALUE

166 LOAD_FAST 0 (self)
168 LOAD_METHOD 6 (_click_recaptcha_checkbox)
170 CALL 0
172 GET_AWAITABLE 0
174 LOAD_CONST 6 (None)
176 SEND 3 (to 182)
178 YIELD_VALUE
180 JUMP_BACKWARD_NO_INTERRUPT 4 (to 176)
182 STORE_FAST 4 (clicked)

184 LOAD_FAST 4 (clicked)
186 POP_JUMP_FORWARD_IF_FALSE 28 (to 210)
188 LOAD_FAST 0 (self)
190 LOAD_METHOD 7 (_is_captcha_solved)
192 CALL 0
194 GET_AWAITABLE 0
196 LOAD_CONST 6 (None)
198 SEND 3 (to 204)
200 YIELD_VALUE
202 JUMP_BACKWARD_NO_INTERRUPT 4 (to 198)
204 POP_JUMP_FORWARD_IF_FALSE 2 (to 210)

206 LOAD_CONST 4 (True)
208 RETURN_VALUE

210 LOAD_FAST 0 (self)
212 LOAD_ATTR 8 (extension_mode)
214 POP_JUMP_FORWARD_IF_FALSE 100 (to 292)

216 LOAD_GLOBAL 1 (NULL + log_automation_step)
218 LOAD_FAST 0 (self)
220 LOAD_ATTR 1 (logger)
222 LOAD_CONST 13 ("CAPTCHA_EXTENSION")
224 LOAD_CONST 14 ("EXTENSION_WAIT")
226 CALL 3
228 POP_TOP

230 LOAD_FAST 0 (self)
232 LOAD_METHOD 9 (_wait_for_manual_captcha_solve)
234 LOAD_CONST 15 (180)
236 KW_NAMES 16 (('timeout',))
238 CALL 1
240 GET_AWAITABLE 0
242 LOAD_CONST 6 (None)
244 SEND 3 (to 250)
246 YIELD_VALUE
248 JUMP_BACKWARD_NO_INTERRUPT 4 (to 244)
250 STORE_FAST 5 (ok)

252 LOAD_FAST 5 (ok)
254 POP_JUMP_FORWARD_IF_FALSE 24 (to 274)

256 LOAD_GLOBAL 1 (NULL + log_automation_step)
258 LOAD_FAST 0 (self)
260 LOAD_ATTR 1 (logger)
262 LOAD_CONST 13 ("CAPTCHA_EXTENSION")
264 LOAD_CONST 17 ("EXTENSION_SOLVED")
266 CALL 3
268 POP_TOP

270 LOAD_CONST 4 (True)
272 RETURN_VALUE

274 LOAD_GLOBAL 1 (NULL + log_automation_step)
276 LOAD_FAST 0 (self)
278 LOAD_ATTR 1 (logger)
280 LOAD_CONST 13 ("CAPTCHA_EXTENSION")
282 LOAD_CONST 18 ("EXTENSION_TIMEOUT")
284 CALL 3
286 POP_TOP

288 LOAD_CONST 8 (False)
290 RETURN_VALUE

292 LOAD_FAST 0 (self)
294 LOAD_ATTR 10 (captcha_solver)
296 POP_JUMP_FORWARD_IF_FALSE 174 (to 424)

298 LOAD_GLOBAL 1 (NULL + log_automation_step)
300 LOAD_FAST 0 (self)
302 LOAD_ATTR 1 (logger)
304 LOAD_CONST 19 ("CAPTCHA_AUTO_SOLVE")
306 LOAD_CONST 2 ("START")
308 CALL 3
310 POP_TOP

312 LOAD_GLOBAL 23 (NULL + asyncio)
314 LOAD_ATTR 12 (sleep)
316 LOAD_CONST 20 (0.5)
318 CALL 1
320 GET_AWAITABLE 0
322 LOAD_CONST 6 (None)
324 SEND 3 (to 330)
326 YIELD_VALUE
328 JUMP_BACKWARD_NO_INTERRUPT 4 (to 324)
330 POP_TOP

332 LOAD_FAST 0 (self)
334 LOAD_METHOD 13 (_solve_audio_captcha)
336 CALL 0
338 GET_AWAITABLE 0
340 LOAD_CONST 6 (None)
342 SEND 3 (to 348)
344 YIELD_VALUE
346 JUMP_BACKWARD_NO_INTERRUPT 4 (to 342)
348 STORE_FAST 6 (solved)

350 LOAD_GLOBAL 23 (NULL + asyncio)
352 LOAD_ATTR 12 (sleep)
354 LOAD_CONST 20 (0.5)
356 CALL 1
358 GET_AWAITABLE 0
360 LOAD_CONST 6 (None)
362 SEND 3 (to 368)
364 YIELD_VALUE
366 JUMP_BACKWARD_NO_INTERRUPT 4 (to 362)
368 POP_TOP

370 LOAD_FAST 6 (solved)
372 POP_JUMP_FORWARD_IF_TRUE 26 (to 392)
374 LOAD_FAST 0 (self)
376 LOAD_METHOD 7 (_is_captcha_solved)
378 CALL 0
380 GET_AWAITABLE 0
382 LOAD_CONST 6 (None)
384 SEND 3 (to 390)
386 YIELD_VALUE
388 JUMP_BACKWARD_NO_INTERRUPT 4 (to 384)
390 POP_JUMP_FORWARD_IF_FALSE 24 (to 410)

392 LOAD_GLOBAL 1 (NULL + log_automation_step)
394 LOAD_FAST 0 (self)
396 LOAD_ATTR 1 (logger)
398 LOAD_CONST 19 ("CAPTCHA_AUTO_SOLVE")
400 LOAD_CONST 21 ("SUCCESS")
402 CALL 3
404 POP_TOP

406 LOAD_CONST 4 (True)
408 RETURN_VALUE

410 LOAD_GLOBAL 1 (NULL + log_automation_step)
412 LOAD_FAST 0 (self)
414 LOAD_ATTR 1 (logger)
416 LOAD_CONST 19 ("CAPTCHA_AUTO_SOLVE")
418 LOAD_CONST 22 ("FAILED")
420 CALL 3
422 POP_TOP

424 LOAD_GLOBAL 1 (NULL + log_automation_step)
426 LOAD_FAST 0 (self)
428 LOAD_ATTR 1 (logger)
430 LOAD_CONST 23 ("CAPTCHA_MANUAL")
432 LOAD_CONST 24 ("WAITING")
434 CALL 3
436 POP_TOP

438 LOAD_FAST 0 (self)
440 LOAD_METHOD 9 (_wait_for_manual_captcha_solve)
442 CALL 0
444 GET_AWAITABLE 0
446 LOAD_CONST 6 (None)
448 SEND 3 (to 454)
450 YIELD_VALUE
452 JUMP_BACKWARD_NO_INTERRUPT 4 (to 448)
454 POP_TOP

456 LOAD_FAST 0 (self)
458 LOAD_METHOD 7 (_is_captcha_solved)
460 CALL 0
462 GET_AWAITABLE 0
464 LOAD_CONST 6 (None)
466 SEND 3 (to 472)
468 YIELD_VALUE
470 JUMP_BACKWARD_NO_INTERRUPT 4 (to 466)
472 POP_JUMP_FORWARD_IF_FALSE 24 (to 492)

474 LOAD_GLOBAL 1 (NULL + log_automation_step)
476 LOAD_FAST 0 (self)
478 LOAD_ATTR 1 (logger)
480 LOAD_CONST 23 ("CAPTCHA_MANUAL")
482 LOAD_CONST 25 ("COMPLETED")
484 CALL 3
486 POP_TOP

488 LOAD_CONST 4 (True)
490 RETURN_VALUE

492 LOAD_GLOBAL 1 (NULL + log_automation_step)
494 LOAD_FAST 0 (self)
496 LOAD_ATTR 1 (logger)
498 LOAD_CONST 23 ("CAPTCHA_MANUAL")
500 LOAD_CONST 26 ("TIMEOUT")
502 CALL 3
504 POP_TOP

506 LOAD_CONST 8 (False)
508 RETURN_VALUE
510 PUSH_EXC_INFO

512 LOAD_GLOBAL 6 (Exception)
514 CHECK_EXC_MATCH
516 POP_JUMP_FORWARD_IF_FALSE 49 (to 564)
518 STORE_FAST 7 (e)

520 LOAD_GLOBAL 1 (NULL + log_automation_step)
522 LOAD_FAST 0 (self)
524 LOAD_ATTR 1 (logger)
526 LOAD_CONST 1 ("CAPTCHA_CHECK")
528 LOAD_CONST 27 ("ERROR")
530 LOAD_CONST 28 ("error")
532 LOAD_GLOBAL 29 (NULL + str)
534 LOAD_FAST 7 (e)
536 CALL 1
538 BUILD_MAP 1
540 CALL 4
542 POP_TOP

544 POP_EXCEPT
546 LOAD_CONST 6 (None)
548 STORE_FAST 7 (e)
550 DELETE_FAST 7 (e)
552 LOAD_CONST 8 (False)
554 RETURN_VALUE
556 LOAD_CONST 6 (None)
558 STORE_FAST 7 (e)
560 DELETE_FAST 7 (e)
562 RERAISE 1

564 RERAISE 0
566 COPY 3
568 POP_EXCEPT
570 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_GLOBAL 1 (NULL + time)
8 LOAD_ATTR 0 (time)
10 CALL 0
12 LOAD_FAST 1 (timeout)
14 BINARY_OP 0
16 STORE_FAST 2 (end)

18 LOAD_GLOBAL 1 (NULL + time)
20 LOAD_ATTR 0 (time)
22 CALL 0
24 LOAD_FAST 2 (end)
26 COMPARE_OP 0 (<)
28 POP_JUMP_FORWARD_IF_FALSE 95 (to 110)

30 NOP

32 LOAD_FAST 0 (self)
34 LOAD_METHOD 1 (_is_captcha_solved)
36 CALL 0
38 GET_AWAITABLE 0
40 LOAD_CONST 1 (None)
42 SEND 3 (to 48)
44 YIELD_VALUE
46 JUMP_BACKWARD_NO_INTERRUPT 4 (to 42)
48 POP_JUMP_FORWARD_IF_FALSE 2 (to 54)

50 LOAD_CONST 2 (True)
52 RETURN_VALUE

54 JUMP_FORWARD 16 (to 78)
56 PUSH_EXC_INFO

58 LOAD_GLOBAL 4 (Exception)
60 CHECK_EXC_MATCH
62 POP_JUMP_FORWARD_IF_FALSE 3 (to 70)
64 POP_TOP

66 POP_EXCEPT
68 JUMP_FORWARD 4 (to 78)

70 RERAISE 0
72 COPY 3
74 POP_EXCEPT
76 RERAISE 1

78 LOAD_GLOBAL 7 (NULL + asyncio)
80 LOAD_ATTR 4 (sleep)
82 LOAD_CONST 3 (2)
84 CALL 1
86 GET_AWAITABLE 0
88 LOAD_CONST 1 (None)
90 SEND 3 (to 96)
92 YIELD_VALUE
94 JUMP_BACKWARD_NO_INTERRUPT 4 (to 90)
96 POP_TOP

98 LOAD_GLOBAL 1 (NULL + time)
100 LOAD_ATTR 0 (time)
102 CALL 0
104 LOAD_FAST 2 (end)
106 COMPARE_OP 0 (<)
108 POP_JUMP_BACKWARD_IF_TRUE 95 (to 30)

110 LOAD_CONST 4 (False)
112 RETURN_VALUE
114 PUSH_EXC_INFO

116 LOAD_GLOBAL 4 (Exception)
118 CHECK_EXC_MATCH
120 POP_JUMP_FORWARD_IF_FALSE 4 (to 130)
122 POP_TOP

124 POP_EXCEPT
126 LOAD_CONST 4 (False)
128 RETURN_VALUE

130 RERAISE 0
132 COPY 3
134 POP_EXCEPT
136 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("AUDIO_CAPTCHA")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_CONST 3 (2)
22 STORE_FAST 1 (max_attempts)

24 LOAD_CONST 4 (0)
26 STORE_FAST 2 (attempt)

28 LOAD_FAST 2 (attempt)
30 LOAD_FAST 1 (max_attempts)
32 COMPARE_OP 0 (<)
34 POP_JUMP_FORWARD_IF_FALSE 36 (to 72)

36 LOAD_FAST 2 (attempt)
38 LOAD_CONST 5 (1)
40 BINARY_OP 13
42 STORE_FAST 2 (attempt)

44 LOAD_GLOBAL 1 (NULL + log_automation_step)
46 LOAD_FAST 0 (self)
48 LOAD_ATTR 1 (logger)
50 LOAD_CONST 1 ("AUDIO_CAPTCHA")
52 LOAD_CONST 6 ("ATTEMPT")
54 LOAD_CONST 7 ("attempt")
56 LOAD_FAST 2 (attempt)
58 BUILD_MAP 1
60 CALL 4
62 POP_TOP

64 LOAD_FAST 2 (attempt)
66 LOAD_FAST 1 (max_attempts)
68 COMPARE_OP 0 (<)
70 POP_JUMP_BACKWARD_IF_TRUE 36 (to 36)

72 LOAD_FAST 0 (self)
74 LOAD_METHOD 2 (_find_recaptcha_frames)
76 CALL 0
78 GET_AWAITABLE 0
80 LOAD_CONST 8 (None)
82 SEND 3 (to 88)
84 YIELD_VALUE
86 JUMP_BACKWARD_NO_INTERRUPT 4 (to 82)
88 UNPACK_SEQUENCE 2
90 STORE_FAST 3 (_)
92 STORE_FAST 4 (challenge_frame)

94 LOAD_FAST 4 (challenge_frame)
96 JUMP_IF_TRUE_OR_POP 6 (to 102)
98 LOAD_FAST 0 (self)
100 LOAD_ATTR 3 (page)
102 STORE_FAST 5 (target)

104 BUILD_LIST 0
106 LOAD_CONST 9 (("button[id='recaptcha-audio-button']", "button[title*='audio']", "button[aria-label*='audio']", "button[aria-label*='Audio challenge']", "button[aria-label*='audio challenge']", '.rc-button-audio', "[role='button']:has-text('audio')", "[role='button']:has-text('Audio')"))
108 LIST_EXTEND 1
110 STORE_FAST 6 (audio_button_selectors)

112 LOAD_CONST 10 (False)
114 STORE_FAST 7 (audio_clicked)

116 LOAD_FAST 6 (audio_button_selectors)
118 GET_ITER
120 FOR_ITER 112 (to 216)
122 STORE_FAST 8 (selector)

124 LOAD_FAST 5 (target)
126 LOAD_METHOD 4 (query_selector)
128 LOAD_FAST 8 (selector)
130 CALL 1
132 GET_AWAITABLE 0
134 LOAD_CONST 8 (None)
136 SEND 3 (to 142)
138 YIELD_VALUE
140 JUMP_BACKWARD_NO_INTERRUPT 4 (to 136)
142 STORE_FAST 9 (element)

144 LOAD_FAST 9 (element)
146 POP_JUMP_FORWARD_IF_FALSE 81 (to 214)

148 LOAD_FAST 9 (element)
150 LOAD_METHOD 5 (click)
152 CALL 0
154 GET_AWAITABLE 0
156 LOAD_CONST 8 (None)
158 SEND 3 (to 164)
160 YIELD_VALUE
162 JUMP_BACKWARD_NO_INTERRUPT 4 (to 158)
164 POP_TOP

166 LOAD_GLOBAL 13 (NULL + asyncio)
168 LOAD_ATTR 7 (sleep)
170 LOAD_CONST 11 (0.5)
172 CALL 1
174 GET_AWAITABLE 0
176 LOAD_CONST 8 (None)
178 SEND 3 (to 184)
180 YIELD_VALUE
182 JUMP_BACKWARD_NO_INTERRUPT 4 (to 178)
184 POP_TOP

186 LOAD_CONST 12 (True)
188 STORE_FAST 7 (audio_clicked)

190 LOAD_GLOBAL 1 (NULL + log_automation_step)
192 LOAD_FAST 0 (self)
194 LOAD_ATTR 1 (logger)
196 LOAD_CONST 1 ("AUDIO_CAPTCHA")
198 LOAD_CONST 13 ("BUTTON_CLICKED")
200 LOAD_CONST 14 ("selector")
202 LOAD_FAST 8 (selector)
204 BUILD_MAP 1
206 CALL 4
208 POP_TOP

210 POP_TOP
212 JUMP_FORWARD 1 (to 216)

214 JUMP_BACKWARD 113 (to 120)

216 LOAD_FAST 7 (audio_clicked)
218 POP_JUMP_FORWARD_IF_TRUE 15 (to 228)

220 LOAD_GLOBAL 17 (NULL + Exception)
222 LOAD_CONST 15 ("Audio captcha button not found")
224 CALL 1
226 RAISE_VARARGS 1 (exception instance)

228 BUILD_LIST 0
230 LOAD_CONST 16 (('audio#audio-source[src]', 'audio[src]', '.rc-audiochallenge-tdownload-link audio[src]', "[src*='.mp3']", "[src*='.wav']", "[src*='audio']"))
232 LIST_EXTEND 1
234 STORE_FAST 10 (audio_selectors)

236 LOAD_CONST 8 (None)
238 STORE_FAST 11 (audio_element)

240 LOAD_CONST 8 (None)
242 STORE_FAST 12 (audio_src)

244 LOAD_FAST 10 (audio_selectors)
246 GET_ITER
248 FOR_ITER 106 (to 354)
250 STORE_FAST 8 (selector)

252 NOP

254 LOAD_FAST 5 (target)
256 LOAD_METHOD 9 (wait_for_selector)
258 LOAD_FAST 8 (selector)
260 LOAD_CONST 17 (2500)
262 KW_NAMES 18 (('timeout',))
264 CALL 2
266 GET_AWAITABLE 0
268 LOAD_CONST 8 (None)
270 SEND 3 (to 276)
272 YIELD_VALUE
274 JUMP_BACKWARD_NO_INTERRUPT 4 (to 270)
276 STORE_FAST 11 (audio_element)

278 LOAD_FAST 11 (audio_element)
280 POP_JUMP_FORWARD_IF_FALSE 56 (to 330)

282 LOAD_FAST 11 (audio_element)
284 LOAD_METHOD 10 (get_attribute)
286 LOAD_CONST 19 ("src")
288 CALL 1
290 GET_AWAITABLE 0
292 LOAD_CONST 8 (None)
294 SEND 3 (to 300)
296 YIELD_VALUE
298 JUMP_BACKWARD_NO_INTERRUPT 4 (to 294)
300 STORE_FAST 12 (audio_src)

302 LOAD_FAST 12 (audio_src)
304 POP_JUMP_FORWARD_IF_FALSE 27 (to 330)

306 LOAD_GLOBAL 1 (NULL + log_automation_step)
308 LOAD_FAST 0 (self)
310 LOAD_ATTR 1 (logger)
312 LOAD_CONST 1 ("AUDIO_CAPTCHA")
314 LOAD_CONST 20 ("AUDIO_FOUND")
316 LOAD_CONST 14 ("selector")
318 LOAD_FAST 8 (selector)
320 BUILD_MAP 1
322 CALL 4
324 POP_TOP

326 POP_TOP
328 JUMP_FORWARD 17 (to 354)
330 JUMP_BACKWARD 91 (to 248)
332 PUSH_EXC_INFO

334 LOAD_GLOBAL 16 (Exception)
336 CHECK_EXC_MATCH
338 POP_JUMP_FORWARD_IF_FALSE 3 (to 346)
340 POP_TOP

342 POP_EXCEPT
344 JUMP_BACKWARD 103 (to 248)

346 RERAISE 0
348 COPY 3
350 POP_EXCEPT
352 RERAISE 1

354 LOAD_FAST 12 (audio_src)
356 POP_JUMP_FORWARD_IF_TRUE 113 (to 476)

358 BUILD_LIST 0
360 LOAD_CONST 21 (('a.rc-audiochallenge-tdownload-link', '#rc-audio .rc-audiochallenge-tdownload a', "a[href*='payload/audio.mp3']", "a[href*='audio']"))
362 LIST_EXTEND 1
364 STORE_FAST 13 (link_selectors)

366 LOAD_FAST 13 (link_selectors)
368 GET_ITER
370 FOR_ITER 106 (to 476)
372 STORE_FAST 8 (selector)

374 NOP

376 LOAD_FAST 5 (target)
378 LOAD_METHOD 4 (query_selector)
380 LOAD_FAST 8 (selector)
382 CALL 1
384 GET_AWAITABLE 0
386 LOAD_CONST 8 (None)
388 SEND 3 (to 394)
390 YIELD_VALUE
392 JUMP_BACKWARD_NO_INTERRUPT 4 (to 388)
394 STORE_FAST 14 (link)

396 LOAD_FAST 14 (link)
398 POP_JUMP_FORWARD_IF_FALSE 58 (to 452)

400 LOAD_FAST 14 (link)
402 LOAD_METHOD 10 (get_attribute)
404 LOAD_CONST 22 ("href")
406 CALL 1
408 GET_AWAITABLE 0
410 LOAD_CONST 8 (None)
412 SEND 3 (to 418)
414 YIELD_VALUE
416 JUMP_BACKWARD_NO_INTERRUPT 4 (to 412)
418 STORE_FAST 15 (href)

420 LOAD_FAST 15 (href)
422 POP_JUMP_FORWARD_IF_FALSE 29 (to 452)

424 LOAD_FAST 15 (href)
426 STORE_FAST 12 (audio_src)

428 LOAD_GLOBAL 1 (NULL + log_automation_step)
430 LOAD_FAST 0 (self)
432 LOAD_ATTR 1 (logger)
434 LOAD_CONST 1 ("AUDIO_CAPTCHA")
436 LOAD_CONST 23 ("AUDIO_LINK_FOUND")
438 LOAD_CONST 14 ("selector")
440 LOAD_FAST 8 (selector)
442 BUILD_MAP 1
444 CALL 4
446 POP_TOP

448 POP_TOP
450 JUMP_FORWARD 17 (to 476)
452 JUMP_BACKWARD 91 (to 370)
454 PUSH_EXC_INFO

456 LOAD_GLOBAL 16 (Exception)
458 CHECK_EXC_MATCH
460 POP_JUMP_FORWARD_IF_FALSE 3 (to 468)
462 POP_TOP

464 POP_EXCEPT
466 JUMP_BACKWARD 103 (to 370)

468 RERAISE 0
470 COPY 3
472 POP_EXCEPT
474 RERAISE 1

476 LOAD_FAST 12 (audio_src)
478 POP_JUMP_FORWARD_IF_FALSE 1176 (to 1508)
480 LOAD_FAST 0 (self)
482 LOAD_ATTR 11 (captcha_solver)
484 POP_JUMP_FORWARD_IF_FALSE 1168 (to 1508)

486 LOAD_GLOBAL 1 (NULL + log_automation_step)
488 LOAD_FAST 0 (self)
490 LOAD_ATTR 1 (logger)
492 LOAD_CONST 1 ("AUDIO_CAPTCHA")
494 LOAD_CONST 24 ("DOWNLOADING")
496 LOAD_CONST 25 ("audio_url")
498 LOAD_FAST 12 (audio_src)
500 LOAD_CONST 8 (None)
502 LOAD_CONST 26 (50)
504 BUILD_SLICE 2
506 BINARY_SUBSCR
508 LOAD_CONST 27 ("...")
510 BINARY_OP 0
512 BUILD_MAP 1
514 CALL 4
516 POP_TOP

518 LOAD_CONST 8 (None)
520 STORE_FAST 16 (audio_bytes)

522 NOP

524 LOAD_CONST 28 (code object is_audio_resp)
526 MAKE_FUNCTION 0 (No arguments)
528 STORE_FAST 17 (is_audio_resp)

530 LOAD_FAST 0 (self)
532 LOAD_ATTR 3 (page)
534 LOAD_METHOD 12 (wait_for_response)
536 LOAD_FAST 17 (is_audio_resp)
538 LOAD_CONST 29 (6000)
540 KW_NAMES 18 (('timeout',))
542 CALL 2
544 GET_AWAITABLE 0
546 LOAD_CONST 8 (None)
548 SEND 3 (to 554)
550 YIELD_VALUE
552 JUMP_BACKWARD_NO_INTERRUPT 4 (to 548)
554 STORE_FAST 18 (resp)

556 LOAD_FAST 18 (resp)
558 LOAD_METHOD 13 (body)
560 CALL 0
562 GET_AWAITABLE 0
564 LOAD_CONST 8 (None)
566 SEND 3 (to 572)
568 YIELD_VALUE
570 JUMP_BACKWARD_NO_INTERRUPT 4 (to 566)
572 STORE_FAST 19 (body)

574 LOAD_FAST 19 (body)
576 POP_JUMP_FORWARD_IF_FALSE 54 (to 618)

578 LOAD_FAST 19 (body)
580 STORE_FAST 16 (audio_bytes)

582 LOAD_GLOBAL 1 (NULL + log_automation_step)
584 LOAD_FAST 0 (self)
586 LOAD_ATTR 1 (logger)
588 LOAD_CONST 1 ("AUDIO_CAPTCHA")
590 LOAD_CONST 30 ("CAPTURED_NETWORK")
592 LOAD_GLOBAL 29 (NULL + len)
594 LOAD_FAST 16 (audio_bytes)
596 CALL 1
598 LOAD_FAST 18 (resp)
600 LOAD_ATTR 15 (url)
602 LOAD_CONST 8 (None)
604 LOAD_CONST 31 (80)
606 BUILD_SLICE 2
608 BINARY_SUBSCR
610 LOAD_CONST 32 (('size', 'url'))
612 BUILD_CONST_KEY_MAP 2
614 CALL 4
616 POP_TOP
618 JUMP_FORWARD 61 (to 680)
620 PUSH_EXC_INFO

622 LOAD_GLOBAL 16 (Exception)
624 CHECK_EXC_MATCH
626 POP_JUMP_FORWARD_IF_FALSE 48 (to 672)
628 STORE_FAST 20 (e)

630 LOAD_GLOBAL 1 (NULL + log_automation_step)
632 LOAD_FAST 0 (self)
634 LOAD_ATTR 1 (logger)
636 LOAD_CONST 1 ("AUDIO_CAPTCHA")
638 LOAD_CONST 33 ("CAPTURE_NETWORK_FAILED")
640 LOAD_CONST 34 ("error")
642 LOAD_GLOBAL 33 (NULL + str)
644 LOAD_FAST 20 (e)
646 CALL 1
648 BUILD_MAP 1
650 CALL 4
652 POP_TOP
654 POP_EXCEPT
656 LOAD_CONST 8 (None)
658 STORE_FAST 20 (e)
660 DELETE_FAST 20 (e)
662 JUMP_FORWARD 8 (to 680)
664 LOAD_CONST 8 (None)
666 STORE_FAST 20 (e)
668 DELETE_FAST 20 (e)
670 RERAISE 1

672 RERAISE 0
674 COPY 3
676 POP_EXCEPT
678 RERAISE 1

680 NOP

682 LOAD_FAST 5 (target)
684 LOAD_METHOD 17 (evaluate)

686 LOAD_CONST 35 ("\n                        async (url) => {\n                          try {\n                            const res = await fetch(url, { credentials: 'include' });\n                            const buf = await res.arrayBuffer();\n                            const bytes = new Uint8Array(buf);\n                            let bin = '';\n                            for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);\n                            return btoa(bin);\n                          } catch (e) { return null; }\n                        }\n                        ")
688 LOAD_FAST 12 (audio_src)

690 CALL 2
692 GET_AWAITABLE 0
694 LOAD_CONST 8 (None)
696 SEND 3 (to 702)
698 YIELD_VALUE
700 JUMP_BACKWARD_NO_INTERRUPT 4 (to 696)
702 STORE_FAST 21 (b64)

704 LOAD_GLOBAL 37 (NULL + isinstance)
706 LOAD_FAST 21 (b64)
708 LOAD_GLOBAL 32 (str)
710 CALL 2
712 POP_JUMP_FORWARD_IF_FALSE 64 (to 760)
714 LOAD_FAST 21 (b64)
716 POP_JUMP_FORWARD_IF_FALSE 62 (to 760)

718 LOAD_GLOBAL 39 (NULL + base64)
720 LOAD_ATTR 20 (b64decode)
722 LOAD_FAST 21 (b64)
724 CALL 1
726 STORE_FAST 22 (decoded)

728 LOAD_FAST 16 (audio_bytes)
730 POP_JUMP_FORWARD_IF_TRUE 2 (to 736)

732 LOAD_FAST 22 (decoded)
734 STORE_FAST 16 (audio_bytes)

736 LOAD_GLOBAL 1 (NULL + log_automation_step)
738 LOAD_FAST 0 (self)
740 LOAD_ATTR 1 (logger)
742 LOAD_CONST 1 ("AUDIO_CAPTCHA")
744 LOAD_CONST 36 ("FETCHED_IN_FRAME")
746 LOAD_CONST 37 ("size")
748 LOAD_GLOBAL 29 (NULL + len)
750 LOAD_FAST 22 (decoded)
752 CALL 1
754 BUILD_MAP 1
756 CALL 4
758 POP_TOP
760 JUMP_FORWARD 61 (to 822)
762 PUSH_EXC_INFO

764 LOAD_GLOBAL 16 (Exception)
766 CHECK_EXC_MATCH
768 POP_JUMP_FORWARD_IF_FALSE 48 (to 814)
770 STORE_FAST 20 (e)

772 LOAD_GLOBAL 1 (NULL + log_automation_step)
774 LOAD_FAST 0 (self)
776 LOAD_ATTR 1 (logger)
778 LOAD_CONST 1 ("AUDIO_CAPTCHA")
780 LOAD_CONST 38 ("FETCH_IN_FRAME_FAILED")
782 LOAD_CONST 34 ("error")
784 LOAD_GLOBAL 33 (NULL + str)
786 LOAD_FAST 20 (e)
788 CALL 1
790 BUILD_MAP 1
792 CALL 4
794 POP_TOP
796 POP_EXCEPT
798 LOAD_CONST 8 (None)
800 STORE_FAST 20 (e)
802 DELETE_FAST 20 (e)
804 JUMP_FORWARD 8 (to 822)
806 LOAD_CONST 8 (None)
808 STORE_FAST 20 (e)
810 DELETE_FAST 20 (e)
812 RERAISE 1

814 RERAISE 0
816 COPY 3
818 POP_EXCEPT
820 RERAISE 1

822 LOAD_FAST 16 (audio_bytes)
824 POP_JUMP_FORWARD_IF_NOT_NONE 142 (to 948)

826 NOP

828 LOAD_CONST 4 (0)
830 LOAD_CONST 8 (None)
832 IMPORT_NAME 21 (requests)
834 STORE_FAST 23 (requests)

836 LOAD_FAST 23 (requests)
838 LOAD_METHOD 22 (get)
840 LOAD_FAST 12 (audio_src)
842 LOAD_CONST 39 (15)
844 KW_NAMES 18 (('timeout',))
846 CALL 2
848 STORE_FAST 24 (r)

850 LOAD_FAST 24 (r)
852 LOAD_ATTR 23 (ok)
854 POP_JUMP_FORWARD_IF_FALSE 45 (to 886)

856 LOAD_FAST 24 (r)
858 LOAD_ATTR 24 (content)
860 STORE_FAST 16 (audio_bytes)

862 LOAD_GLOBAL 1 (NULL + log_automation_step)
864 LOAD_FAST 0 (self)
866 LOAD_ATTR 1 (logger)
868 LOAD_CONST 1 ("AUDIO_CAPTCHA")
870 LOAD_CONST 40 ("FETCHED_REQUESTS")
872 LOAD_CONST 37 ("size")
874 LOAD_GLOBAL 29 (NULL + len)
876 LOAD_FAST 16 (audio_bytes)
878 CALL 1
880 BUILD_MAP 1
882 CALL 4
884 POP_TOP
886 JUMP_FORWARD 61 (to 948)
888 PUSH_EXC_INFO

890 LOAD_GLOBAL 16 (Exception)
892 CHECK_EXC_MATCH
894 POP_JUMP_FORWARD_IF_FALSE 48 (to 940)
896 STORE_FAST 20 (e)

898 LOAD_GLOBAL 1 (NULL + log_automation_step)
900 LOAD_FAST 0 (self)
902 LOAD_ATTR 1 (logger)
904 LOAD_CONST 1 ("AUDIO_CAPTCHA")
906 LOAD_CONST 41 ("FETCH_REQUESTS_FAILED")
908 LOAD_CONST 34 ("error")
910 LOAD_GLOBAL 33 (NULL + str)
912 LOAD_FAST 20 (e)
914 CALL 1
916 BUILD_MAP 1
918 CALL 4
920 POP_TOP
922 POP_EXCEPT
924 LOAD_CONST 8 (None)
926 STORE_FAST 20 (e)
928 DELETE_FAST 20 (e)
930 JUMP_FORWARD 8 (to 948)
932 LOAD_CONST 8 (None)
934 STORE_FAST 20 (e)
936 DELETE_FAST 20 (e)
938 RERAISE 1

940 RERAISE 0
942 COPY 3
944 POP_EXCEPT
946 RERAISE 1

948 LOAD_FAST 16 (audio_bytes)
950 POP_JUMP_FORWARD_IF_TRUE 27 (to 976)

952 LOAD_GLOBAL 1 (NULL + log_automation_step)
954 LOAD_FAST 0 (self)
956 LOAD_ATTR 1 (logger)
958 LOAD_CONST 1 ("AUDIO_CAPTCHA")
960 LOAD_CONST 42 ("ERROR")
962 LOAD_CONST 34 ("error")
964 LOAD_CONST 43 ("Unable to download audio")
966 BUILD_MAP 1
968 CALL 4
970 POP_TOP

972 LOAD_CONST 10 (False)
974 RETURN_VALUE

976 LOAD_CONST 44 (".mp3")
978 LOAD_FAST 12 (audio_src)
980 JUMP_IF_TRUE_OR_POP 1 (to 984)
982 LOAD_CONST 45 ("")
984 LOAD_METHOD 25 (lower)
986 CALL 0
988 CONTAINS_OP 0 (in)
990 POP_JUMP_FORWARD_IF_FALSE 2 (to 996)
992 LOAD_CONST 46 ("mp3")
994 JUMP_FORWARD 1 (to 998)
996 LOAD_CONST 47 ("wav")
998 STORE_FAST 25 (fmt)

1000 LOAD_FAST 0 (self)
1002 LOAD_ATTR 11 (captcha_solver)
1004 LOAD_METHOD 26 (solve_audio_captcha_from_bytes)
1006 LOAD_FAST 16 (audio_bytes)
1008 LOAD_FAST 25 (fmt)
1010 KW_NAMES 48 (('format',))
1012 CALL 2
1014 STORE_FAST 26 (result)

1016 LOAD_FAST 26 (result)
1018 POP_JUMP_FORWARD_IF_FALSE 513 (to 1484)

1020 LOAD_GLOBAL 1 (NULL + log_automation_step)
1022 LOAD_FAST 0 (self)
1024 LOAD_ATTR 1 (logger)
1026 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1028 LOAD_CONST 49 ("SOLVED")
1030 LOAD_CONST 50 ("result")
1032 LOAD_FAST 26 (result)
1034 BUILD_MAP 1
1036 CALL 4
1038 POP_TOP

1040 BUILD_LIST 0
1042 LOAD_CONST 51 (("input[id='audio-response']", "input[name='audio-response']", '.rc-audiochallenge-response-field', "input[type='text']:visible", "input[placeholder*='hear']", "input[aria-label*='audio']"))
1044 LIST_EXTEND 1
1046 STORE_FAST 27 (input_selectors)

1048 LOAD_CONST 10 (False)
1050 STORE_FAST 28 (input_filled)

1052 LOAD_FAST 27 (input_selectors)
1054 GET_ITER
1056 FOR_ITER 113 (to 1154)
1058 STORE_FAST 8 (selector)

1060 LOAD_FAST 5 (target)
1062 LOAD_METHOD 4 (query_selector)
1064 LOAD_FAST 8 (selector)
1066 CALL 1
1068 GET_AWAITABLE 0
1070 LOAD_CONST 8 (None)
1072 SEND 3 (to 1078)
1074 YIELD_VALUE
1076 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1072)
1078 STORE_FAST 29 (text_input)

1080 LOAD_FAST 29 (text_input)
1082 POP_JUMP_FORWARD_IF_FALSE 82 (to 1152)

1084 LOAD_FAST 29 (text_input)
1086 LOAD_METHOD 27 (fill)
1088 LOAD_FAST 26 (result)
1090 CALL 1
1092 GET_AWAITABLE 0
1094 LOAD_CONST 8 (None)
1096 SEND 3 (to 1102)
1098 YIELD_VALUE
1100 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1096)
1102 POP_TOP

1104 LOAD_GLOBAL 13 (NULL + asyncio)
1106 LOAD_ATTR 7 (sleep)
1108 LOAD_CONST 11 (0.5)
1110 CALL 1
1112 GET_AWAITABLE 0
1114 LOAD_CONST 8 (None)
1116 SEND 3 (to 1122)
1118 YIELD_VALUE
1120 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1116)
1122 POP_TOP

1124 LOAD_CONST 12 (True)
1126 STORE_FAST 28 (input_filled)

1128 LOAD_GLOBAL 1 (NULL + log_automation_step)
1130 LOAD_FAST 0 (self)
1132 LOAD_ATTR 1 (logger)
1134 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1136 LOAD_CONST 52 ("INPUT_FILLED")
1138 LOAD_CONST 14 ("selector")
1140 LOAD_FAST 8 (selector)
1142 BUILD_MAP 1
1144 CALL 4
1146 POP_TOP

1148 POP_TOP
1150 JUMP_FORWARD 1 (to 1154)

1152 JUMP_BACKWARD 114 (to 1056)

1154 LOAD_FAST 28 (input_filled)
1156 POP_JUMP_FORWARD_IF_FALSE 336 (to 1460)

1158 BUILD_LIST 0
1160 LOAD_CONST 53 (("button[id='recaptcha-verify-button']", "button:has-text('Verify')", "button:has-text('Submit')", '.rc-audiochallenge-verify-button', "input[type='submit']", "button[type='submit']"))
1162 LIST_EXTEND 1
1164 STORE_FAST 30 (submit_selectors)

1166 LOAD_FAST 30 (submit_selectors)
1168 GET_ITER
1170 FOR_ITER 301 (to 1436)
1172 STORE_FAST 8 (selector)

1174 LOAD_FAST 5 (target)
1176 LOAD_METHOD 4 (query_selector)
1178 LOAD_FAST 8 (selector)
1180 CALL 1
1182 GET_AWAITABLE 0
1184 LOAD_CONST 8 (None)
1186 SEND 3 (to 1192)
1188 YIELD_VALUE
1190 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1186)
1192 STORE_FAST 31 (submit_btn)

1194 LOAD_FAST 31 (submit_btn)
1196 POP_JUMP_FORWARD_IF_FALSE 268 (to 1434)

1198 LOAD_FAST 31 (submit_btn)
1200 LOAD_METHOD 5 (click)
1202 CALL 0
1204 GET_AWAITABLE 0
1206 LOAD_CONST 8 (None)
1208 SEND 3 (to 1214)
1210 YIELD_VALUE
1212 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1208)
1214 POP_TOP

1216 LOAD_GLOBAL 13 (NULL + asyncio)
1218 LOAD_ATTR 7 (sleep)
1220 LOAD_CONST 54 (1.0)
1222 CALL 1
1224 GET_AWAITABLE 0
1226 LOAD_CONST 8 (None)
1228 SEND 3 (to 1234)
1230 YIELD_VALUE
1232 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1228)
1234 POP_TOP

1236 LOAD_FAST 0 (self)
1238 LOAD_METHOD 28 (_is_captcha_solved)
1240 CALL 0
1242 GET_AWAITABLE 0
1244 LOAD_CONST 8 (None)
1246 SEND 3 (to 1252)
1248 YIELD_VALUE
1250 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1246)
1252 POP_JUMP_FORWARD_IF_FALSE 29 (to 1282)

1254 LOAD_GLOBAL 1 (NULL + log_automation_step)
1256 LOAD_FAST 0 (self)
1258 LOAD_ATTR 1 (logger)
1260 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1262 LOAD_CONST 55 ("SUCCESS")
1264 LOAD_FAST 26 (result)
1266 LOAD_FAST 2 (attempt)
1268 LOAD_CONST 56 (('result', 'attempt'))
1270 BUILD_CONST_KEY_MAP 2
1272 CALL 4
1274 POP_TOP

1276 POP_TOP
1278 LOAD_CONST 12 (True)
1280 RETURN_VALUE

1282 LOAD_GLOBAL 1 (NULL + log_automation_step)
1284 LOAD_FAST 0 (self)
1286 LOAD_ATTR 1 (logger)
1288 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1290 LOAD_CONST 57 ("VERIFY_FAILED")
1292 LOAD_CONST 7 ("attempt")
1294 LOAD_FAST 2 (attempt)
1296 BUILD_MAP 1
1298 CALL 4
1300 POP_TOP

1302 BUILD_LIST 0
1304 LOAD_CONST 58 (('.rc-button-reload', 'button#recaptcha-reload-button', "button[aria-label*='reload']", "button:has-text('Get a new challenge')"))
1306 LIST_EXTEND 1
1308 STORE_FAST 32 (reload_selectors)

1310 LOAD_FAST 32 (reload_selectors)
1312 GET_ITER
1314 FOR_ITER 101 (to 1410)
1316 STORE_FAST 33 (rs)

1318 NOP

1320 LOAD_FAST 5 (target)
1322 LOAD_METHOD 4 (query_selector)
1324 LOAD_FAST 33 (rs)
1326 CALL 1
1328 GET_AWAITABLE 0
1330 LOAD_CONST 8 (None)
1332 SEND 3 (to 1338)
1334 YIELD_VALUE
1336 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1332)
1338 STORE_FAST 34 (rb)

1340 LOAD_FAST 34 (rb)
1342 POP_JUMP_FORWARD_IF_FALSE 53 (to 1386)

1344 LOAD_FAST 34 (rb)
1346 LOAD_METHOD 5 (click)
1348 CALL 0
1350 GET_AWAITABLE 0
1352 LOAD_CONST 8 (None)
1354 SEND 3 (to 1360)
1356 YIELD_VALUE
1358 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1354)
1360 POP_TOP

1362 LOAD_GLOBAL 1 (NULL + log_automation_step)
1364 LOAD_FAST 0 (self)
1366 LOAD_ATTR 1 (logger)
1368 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1370 LOAD_CONST 59 ("RELOAD_CLICKED")
1372 LOAD_CONST 14 ("selector")
1374 LOAD_FAST 33 (rs)
1376 BUILD_MAP 1
1378 CALL 4
1380 POP_TOP

1382 POP_TOP
1384 JUMP_FORWARD 17 (to 1410)

1386 JUMP_BACKWARD 86 (to 1314)
1388 PUSH_EXC_INFO

1390 LOAD_GLOBAL 16 (Exception)
1392 CHECK_EXC_MATCH
1394 POP_JUMP_FORWARD_IF_FALSE 3 (to 1402)
1396 POP_TOP

1398 POP_EXCEPT
1400 JUMP_BACKWARD 98 (to 1314)

1402 RERAISE 0
1404 COPY 3
1406 POP_EXCEPT
1408 RERAISE 1

1410 LOAD_GLOBAL 13 (NULL + asyncio)
1412 LOAD_ATTR 7 (sleep)
1414 LOAD_CONST 54 (1.0)
1416 CALL 1
1418 GET_AWAITABLE 0
1420 LOAD_CONST 8 (None)
1422 SEND 3 (to 1428)
1424 YIELD_VALUE
1426 JUMP_BACKWARD_NO_INTERRUPT 4 (to 1422)
1428 POP_TOP

1430 POP_TOP
1432 JUMP_FORWARD 2 (to 1436)

1434 JUMP_BACKWARD 303 (to 1170)

1436 LOAD_GLOBAL 1 (NULL + log_automation_step)
1438 LOAD_FAST 0 (self)
1440 LOAD_ATTR 1 (logger)
1442 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1444 LOAD_CONST 42 ("ERROR")
1446 LOAD_CONST 34 ("error")
1448 LOAD_CONST 60 ("Submit button not found")
1450 BUILD_MAP 1
1452 CALL 4
1454 POP_TOP
1456 LOAD_CONST 8 (None)
1458 RETURN_VALUE

1460 LOAD_GLOBAL 1 (NULL + log_automation_step)
1462 LOAD_FAST 0 (self)
1464 LOAD_ATTR 1 (logger)
1466 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1468 LOAD_CONST 42 ("ERROR")
1470 LOAD_CONST 34 ("error")
1472 LOAD_CONST 61 ("Text input field not found")
1474 BUILD_MAP 1
1476 CALL 4
1478 POP_TOP
1480 LOAD_CONST 8 (None)
1482 RETURN_VALUE

1484 LOAD_GLOBAL 1 (NULL + log_automation_step)
1486 LOAD_FAST 0 (self)
1488 LOAD_ATTR 1 (logger)
1490 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1492 LOAD_CONST 42 ("ERROR")
1494 LOAD_CONST 34 ("error")
1496 LOAD_CONST 62 ("Could not solve audio captcha")
1498 BUILD_MAP 1
1500 CALL 4
1502 POP_TOP
1504 LOAD_CONST 8 (None)
1506 RETURN_VALUE

1508 LOAD_GLOBAL 1 (NULL + log_automation_step)
1510 LOAD_FAST 0 (self)
1512 LOAD_ATTR 1 (logger)
1514 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1516 LOAD_CONST 42 ("ERROR")
1518 LOAD_CONST 34 ("error")
1520 LOAD_CONST 63 ("Audio source not found or captcha solver not available")
1522 BUILD_MAP 1
1524 CALL 4
1526 POP_TOP

1528 LOAD_CONST 10 (False)
1530 RETURN_VALUE
1532 PUSH_EXC_INFO

1534 LOAD_GLOBAL 16 (Exception)
1536 CHECK_EXC_MATCH
1538 POP_JUMP_FORWARD_IF_FALSE 49 (to 1586)
1540 STORE_FAST 20 (e)

1542 LOAD_GLOBAL 1 (NULL + log_automation_step)
1544 LOAD_FAST 0 (self)
1546 LOAD_ATTR 1 (logger)
1548 LOAD_CONST 1 ("AUDIO_CAPTCHA")
1550 LOAD_CONST 42 ("ERROR")
1552 LOAD_CONST 34 ("error")
1554 LOAD_GLOBAL 33 (NULL + str)
1556 LOAD_FAST 20 (e)
1558 CALL 1
1560 BUILD_MAP 1
1562 CALL 4
1564 POP_TOP

1566 POP_EXCEPT
1568 LOAD_CONST 8 (None)
1570 STORE_FAST 20 (e)
1572 DELETE_FAST 20 (e)
1574 LOAD_CONST 10 (False)
1576 RETURN_VALUE
1578 LOAD_CONST 8 (None)
1580 STORE_FAST 20 (e)
1582 DELETE_FAST 20 (e)
1584 RERAISE 1

1586 RERAISE 0
1588 COPY 3
1590 POP_EXCEPT
1592 RERAISE 1


0 LOAD_FAST 0 (resp)
2 LOAD_ATTR 0 (url)
4 JUMP_IF_TRUE_OR_POP 1 (to 8)
6 LOAD_CONST 1 ("")
8 LOAD_METHOD 1 (lower)
10 CALL 0
12 STORE_FAST 1 (url)

14 LOAD_FAST 0 (resp)
16 LOAD_ATTR 2 (headers)
18 LOAD_METHOD 3 (get)
20 LOAD_CONST 2 ("content-type")
22 CALL 1
24 JUMP_IF_TRUE_OR_POP 1 (to 28)
26 LOAD_CONST 1 ("")
28 LOAD_METHOD 1 (lower)
30 CALL 0
32 STORE_FAST 2 (ctype)

34 LOAD_CONST 3 ("recaptcha")
36 LOAD_FAST 1 (url)
38 CONTAINS_OP 0 (in)
40 POP_JUMP_FORWARD_IF_FALSE 29 (to 68)
42 LOAD_CONST 4 ("audio")
44 LOAD_FAST 1 (url)
46 CONTAINS_OP 0 (in)
48 JUMP_IF_TRUE_OR_POP 28 (to 74)
50 LOAD_FAST 1 (url)
52 LOAD_METHOD 4 (endswith)
54 LOAD_CONST 5 (".mp3")
56 CALL 1
58 JUMP_IF_TRUE_OR_POP 7 (to 74)
60 LOAD_CONST 5 (".mp3")
62 LOAD_FAST 1 (url)
64 CONTAINS_OP 0 (in)
66 JUMP_IF_TRUE_OR_POP 3 (to 74)
68 LOAD_CONST 6 ("audio/")
70 LOAD_FAST 2 (ctype)
72 CONTAINS_OP 0 (in)
74 RETURN_VALUE


0 RETURN_GENERATOR
2 POP_TOP

4 NOP

6 LOAD_FAST 0 (self)
8 LOAD_ATTR 0 (page)
10 LOAD_METHOD 1 (evaluate)

12 LOAD_CONST 1 ('\n                try {\n                  const t = document.querySelector(\'textarea#g-recaptcha-response, textarea[name="g-recaptcha-response"]\');\n                  return t && t.value ? t.value : \'\';\n                } catch(e) { return \'\'; }\n                ')
14 CALL 1
16 GET_AWAITABLE 0
18 LOAD_CONST 2 (None)
20 SEND 3 (to 26)
22 YIELD_VALUE
24 JUMP_BACKWARD_NO_INTERRUPT 4 (to 20)
26 STORE_FAST 1 (token)
28 JUMP_FORWARD 18 (to 56)
30 PUSH_EXC_INFO

32 LOAD_GLOBAL 4 (Exception)
34 CHECK_EXC_MATCH
36 POP_JUMP_FORWARD_IF_FALSE 5 (to 48)
38 POP_TOP

40 LOAD_CONST 3 ("")
42 STORE_FAST 1 (token)
44 POP_EXCEPT
46 JUMP_FORWARD 4 (to 56)

48 RERAISE 0
50 COPY 3
52 POP_EXCEPT
54 RERAISE 1

56 LOAD_GLOBAL 7 (NULL + isinstance)
58 LOAD_FAST 1 (token)
60 LOAD_GLOBAL 8 (str)
62 CALL 2
64 POP_JUMP_FORWARD_IF_FALSE 22 (to 78)
66 LOAD_FAST 1 (token)
68 LOAD_METHOD 5 (strip)
70 CALL 0
72 POP_JUMP_FORWARD_IF_FALSE 2 (to 78)

74 LOAD_CONST 4 (True)
76 RETURN_VALUE

78 NOP

80 LOAD_FAST 0 (self)
82 LOAD_ATTR 0 (page)
84 LOAD_ATTR 6 (frames)
86 GET_ITER
88 FOR_ITER 70 (to 170)
90 STORE_FAST 2 (fr)

92 LOAD_CONST 5 ("recaptcha")
94 LOAD_FAST 2 (fr)
96 LOAD_ATTR 7 (url)
98 CONTAINS_OP 0 (in)
100 POP_JUMP_FORWARD_IF_TRUE 9 (to 112)
102 LOAD_CONST 6 ("google.com/recaptcha")
104 LOAD_FAST 2 (fr)
106 LOAD_ATTR 7 (url)
108 CONTAINS_OP 0 (in)
110 POP_JUMP_FORWARD_IF_FALSE 50 (to 168)

112 NOP

114 LOAD_FAST 2 (fr)
116 LOAD_METHOD 8 (query_selector)
118 LOAD_CONST 7 ("#recaptcha-anchor[aria-checked='true'], span.recaptcha-checkbox-checked[role='checkbox']")
120 CALL 1
122 GET_AWAITABLE 0
124 LOAD_CONST 2 (None)
126 SEND 3 (to 132)
128 YIELD_VALUE
130 JUMP_BACKWARD_NO_INTERRUPT 4 (to 126)
132 STORE_FAST 3 (el)

134 LOAD_FAST 3 (el)
136 POP_JUMP_FORWARD_IF_FALSE 3 (to 144)

138 POP_TOP
140 LOAD_CONST 4 (True)
142 RETURN_VALUE

144 JUMP_BACKWARD 54 (to 88)
146 PUSH_EXC_INFO

148 LOAD_GLOBAL 4 (Exception)
150 CHECK_EXC_MATCH
152 POP_JUMP_FORWARD_IF_FALSE 3 (to 160)
154 POP_TOP

156 POP_EXCEPT
158 JUMP_BACKWARD 66 (to 88)

160 RERAISE 0
162 COPY 3
164 POP_EXCEPT
166 RERAISE 1

168 JUMP_BACKWARD 71 (to 88)

170 JUMP_FORWARD 16 (to 194)
172 PUSH_EXC_INFO

174 LOAD_GLOBAL 4 (Exception)
176 CHECK_EXC_MATCH
178 POP_JUMP_FORWARD_IF_FALSE 3 (to 186)
180 POP_TOP

182 POP_EXCEPT
184 JUMP_FORWARD 4 (to 194)

186 RERAISE 0
188 COPY 3
190 POP_EXCEPT
192 RERAISE 1

194 NOP

196 LOAD_FAST 0 (self)
198 LOAD_ATTR 0 (page)
200 LOAD_METHOD 8 (query_selector)
202 LOAD_CONST 8 ("iframe[title*='reCAPTCHA'], iframe[src*='recaptcha']")
204 CALL 1
206 GET_AWAITABLE 0
208 LOAD_CONST 2 (None)
210 SEND 3 (to 216)
212 YIELD_VALUE
214 JUMP_BACKWARD_NO_INTERRUPT 4 (to 210)
216 STORE_FAST 4 (rec_iframe)

218 LOAD_FAST 4 (rec_iframe)
220 LOAD_CONST 2 (None)
222 IS_OP 0 (is)
224 RETURN_VALUE
226 PUSH_EXC_INFO

228 LOAD_GLOBAL 4 (Exception)
230 CHECK_EXC_MATCH
232 POP_JUMP_FORWARD_IF_FALSE 4 (to 242)
234 POP_TOP

236 POP_EXCEPT
238 LOAD_CONST 9 (False)
240 RETURN_VALUE

242 RERAISE 0
244 COPY 3
246 POP_EXCEPT
248 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("FORM_SUBMIT")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_FAST 0 (self)
22 LOAD_METHOD 2 (_is_captcha_solved)
24 CALL 0
26 GET_AWAITABLE 0
28 LOAD_CONST 3 (None)
30 SEND 3 (to 36)
32 YIELD_VALUE
34 JUMP_BACKWARD_NO_INTERRUPT 4 (to 30)
36 POP_JUMP_FORWARD_IF_TRUE 15 (to 46)

38 LOAD_GLOBAL 7 (NULL + Exception)
40 LOAD_CONST 4 ("Attempted to submit while CAPTCHA not solved")
42 CALL 1
44 RAISE_VARARGS 1 (exception instance)

46 LOAD_FAST 0 (self)
48 LOAD_ATTR 4 (page)
50 LOAD_METHOD 5 (query_selector)
52 LOAD_CONST 5 ("button[id='accountDetailsNext']")
54 CALL 1
56 GET_AWAITABLE 0
58 LOAD_CONST 3 (None)
60 SEND 3 (to 66)
62 YIELD_VALUE
64 JUMP_BACKWARD_NO_INTERRUPT 4 (to 60)
66 STORE_FAST 1 (next_button)

68 LOAD_FAST 1 (next_button)
70 POP_JUMP_FORWARD_IF_TRUE 32 (to 94)

72 LOAD_FAST 0 (self)
74 LOAD_ATTR 4 (page)
76 LOAD_METHOD 5 (query_selector)
78 LOAD_CONST 6 ("button:has-text('Next')")
80 CALL 1
82 GET_AWAITABLE 0
84 LOAD_CONST 3 (None)
86 SEND 3 (to 92)
88 YIELD_VALUE
90 JUMP_BACKWARD_NO_INTERRUPT 4 (to 86)
92 STORE_FAST 1 (next_button)

94 LOAD_FAST 1 (next_button)
96 POP_JUMP_FORWARD_IF_TRUE 32 (to 120)

98 LOAD_FAST 0 (self)
100 LOAD_ATTR 4 (page)
102 LOAD_METHOD 5 (query_selector)
104 LOAD_CONST 7 ("button[type='submit']")
106 CALL 1
108 GET_AWAITABLE 0
110 LOAD_CONST 3 (None)
112 SEND 3 (to 118)
114 YIELD_VALUE
116 JUMP_BACKWARD_NO_INTERRUPT 4 (to 112)
118 STORE_FAST 1 (next_button)

120 LOAD_FAST 1 (next_button)
122 POP_JUMP_FORWARD_IF_FALSE 76 (to 180)

124 LOAD_FAST 1 (next_button)
126 LOAD_METHOD 6 (click)
128 CALL 0
130 GET_AWAITABLE 0
132 LOAD_CONST 3 (None)
134 SEND 3 (to 140)
136 YIELD_VALUE
138 JUMP_BACKWARD_NO_INTERRUPT 4 (to 134)
140 POP_TOP

142 LOAD_GLOBAL 15 (NULL + asyncio)
144 LOAD_ATTR 8 (sleep)
146 LOAD_CONST 8 (2)
148 CALL 1
150 GET_AWAITABLE 0
152 LOAD_CONST 3 (None)
154 SEND 3 (to 160)
156 YIELD_VALUE
158 JUMP_BACKWARD_NO_INTERRUPT 4 (to 154)
160 POP_TOP

162 LOAD_GLOBAL 1 (NULL + log_automation_step)
164 LOAD_FAST 0 (self)
166 LOAD_ATTR 1 (logger)
168 LOAD_CONST 1 ("FORM_SUBMIT")
170 LOAD_CONST 9 ("SUCCESS")
172 CALL 3
174 POP_TOP
176 LOAD_CONST 3 (None)
178 RETURN_VALUE

180 LOAD_GLOBAL 7 (NULL + Exception)
182 LOAD_CONST 10 ("Submit button not found")
184 CALL 1
186 RAISE_VARARGS 1 (exception instance)
188 PUSH_EXC_INFO

190 LOAD_GLOBAL 6 (Exception)
192 CHECK_EXC_MATCH
194 POP_JUMP_FORWARD_IF_FALSE 44 (to 232)
196 STORE_FAST 2 (e)

198 LOAD_GLOBAL 1 (NULL + log_automation_step)
200 LOAD_FAST 0 (self)
202 LOAD_ATTR 1 (logger)
204 LOAD_CONST 1 ("FORM_SUBMIT")
206 LOAD_CONST 11 ("ERROR")
208 LOAD_CONST 12 ("error")
210 LOAD_GLOBAL 19 (NULL + str)
212 LOAD_FAST 2 (e)
214 CALL 1
216 BUILD_MAP 1
218 CALL 4
220 POP_TOP

222 RAISE_VARARGS 0 (reraise)
224 LOAD_CONST 3 (None)
226 STORE_FAST 2 (e)
228 DELETE_FAST 2 (e)
230 RERAISE 1

232 RERAISE 0
234 COPY 3
236 POP_EXCEPT
238 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("RESULT_WAITING")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 NOP

20 LOAD_FAST 0 (self)
22 LOAD_ATTR 2 (page)
24 LOAD_METHOD 3 (wait_for_load_state)
26 LOAD_CONST 3 ("networkidle")
28 LOAD_CONST 4 (30000)
30 KW_NAMES 5 (('timeout',))
32 CALL 2
34 GET_AWAITABLE 0
36 LOAD_CONST 6 (None)
38 SEND 3 (to 44)
40 YIELD_VALUE
42 JUMP_BACKWARD_NO_INTERRUPT 4 (to 38)
44 POP_TOP

46 LOAD_FAST 0 (self)
48 LOAD_ATTR 2 (page)
50 LOAD_ATTR 4 (url)
52 STORE_FAST 1 (current_url)

54 LOAD_CONST 7 ("signup")
56 LOAD_FAST 1 (current_url)
58 LOAD_METHOD 5 (lower)
60 CALL 0
62 CONTAINS_OP 1 (not in)
64 POP_JUMP_FORWARD_IF_FALSE 31 (to 98)

66 LOAD_GLOBAL 1 (NULL + log_automation_step)
68 LOAD_FAST 0 (self)
70 LOAD_ATTR 1 (logger)
72 LOAD_CONST 1 ("RESULT_WAITING")
74 LOAD_CONST 8 ("SUCCESS")
76 LOAD_CONST 9 ("url")
78 LOAD_FAST 1 (current_url)
80 BUILD_MAP 1
82 CALL 4
84 POP_TOP

86 LOAD_CONST 10 (True)
88 LOAD_CONST 11 ("Registration completed")
90 LOAD_FAST 1 (current_url)
92 LOAD_CONST 12 (('success', 'message', 'url'))
94 BUILD_CONST_KEY_MAP 3
96 RETURN_VALUE

98 LOAD_FAST 0 (self)
100 LOAD_ATTR 2 (page)
102 LOAD_METHOD 6 (query_selector_all)
104 LOAD_CONST 13 (".VfPpkd-CmumD-MZAGBe-SIawsf")
106 CALL 1
108 GET_AWAITABLE 0
110 LOAD_CONST 6 (None)
112 SEND 3 (to 118)
114 YIELD_VALUE
116 JUMP_BACKWARD_NO_INTERRUPT 4 (to 112)
118 STORE_FAST 2 (error_elements)

120 LOAD_FAST 2 (error_elements)
122 POP_JUMP_FORWARD_IF_FALSE 145 (to 222)

124 BUILD_LIST 0
126 STORE_FAST 3 (error_messages)

128 LOAD_FAST 2 (error_elements)
130 GET_ITER
132 FOR_ITER 87 (to 178)
134 STORE_FAST 4 (element)

136 LOAD_FAST 4 (element)
138 LOAD_METHOD 7 (inner_text)
140 CALL 0
142 GET_AWAITABLE 0
144 LOAD_CONST 6 (None)
146 SEND 3 (to 152)
148 YIELD_VALUE
150 JUMP_BACKWARD_NO_INTERRUPT 4 (to 146)
152 STORE_FAST 5 (text)

154 LOAD_FAST 5 (text)
156 LOAD_METHOD 8 (strip)
158 CALL 0
160 POP_JUMP_FORWARD_IF_FALSE 39 (to 176)

162 LOAD_FAST 3 (error_messages)
164 LOAD_METHOD 9 (append)
166 LOAD_FAST 5 (text)
168 LOAD_METHOD 8 (strip)
170 CALL 0
172 CALL 1
174 POP_TOP
176 JUMP_BACKWARD 88 (to 132)

178 LOAD_FAST 3 (error_messages)
180 POP_JUMP_FORWARD_IF_FALSE 51 (to 222)

182 LOAD_CONST 14 ("; ")
184 LOAD_METHOD 10 (join)
186 LOAD_FAST 3 (error_messages)
188 CALL 1
190 STORE_FAST 6 (error_msg)

192 LOAD_GLOBAL 1 (NULL + log_automation_step)
194 LOAD_FAST 0 (self)
196 LOAD_ATTR 1 (logger)
198 LOAD_CONST 1 ("RESULT_WAITING")
200 LOAD_CONST 15 ("ERROR")
202 LOAD_CONST 16 ("errors")
204 LOAD_FAST 3 (error_messages)
206 BUILD_MAP 1
208 CALL 4
210 POP_TOP

212 LOAD_CONST 17 (False)
214 LOAD_FAST 6 (error_msg)
216 LOAD_CONST 18 (('success', 'error'))
218 BUILD_CONST_KEY_MAP 2
220 RETURN_VALUE

222 LOAD_GLOBAL 1 (NULL + log_automation_step)
224 LOAD_FAST 0 (self)
226 LOAD_ATTR 1 (logger)
228 LOAD_CONST 1 ("RESULT_WAITING")
230 LOAD_CONST 19 ("UNKNOWN")
232 CALL 3
234 POP_TOP

236 LOAD_CONST 17 (False)
238 LOAD_CONST 20 ("Unknown result - still on signup page")
240 LOAD_CONST 18 (('success', 'error'))
242 BUILD_CONST_KEY_MAP 2
244 RETURN_VALUE
246 PUSH_EXC_INFO

248 LOAD_GLOBAL 22 (Exception)
250 CHECK_EXC_MATCH
252 POP_JUMP_FORWARD_IF_FALSE 69 (to 318)
254 STORE_FAST 7 (e)

256 LOAD_GLOBAL 1 (NULL + log_automation_step)
258 LOAD_FAST 0 (self)
260 LOAD_ATTR 1 (logger)
262 LOAD_CONST 1 ("RESULT_WAITING")
264 LOAD_CONST 15 ("ERROR")
266 LOAD_CONST 21 ("error")
268 LOAD_GLOBAL 25 (NULL + str)
270 LOAD_FAST 7 (e)
272 CALL 1
274 BUILD_MAP 1
276 CALL 4
278 POP_TOP

280 LOAD_CONST 17 (False)
282 LOAD_CONST 22 ("Error waiting for result: ")
284 LOAD_GLOBAL 25 (NULL + str)
286 LOAD_FAST 7 (e)
288 CALL 1
290 FORMAT_VALUE 0
292 BUILD_STRING 2
294 LOAD_CONST 18 (('success', 'error'))
296 BUILD_CONST_KEY_MAP 2
298 SWAP 2
300 POP_EXCEPT
302 LOAD_CONST 6 (None)
304 STORE_FAST 7 (e)
306 DELETE_FAST 7 (e)
308 RETURN_VALUE
310 LOAD_CONST 6 (None)
312 STORE_FAST 7 (e)
314 DELETE_FAST 7 (e)
316 RERAISE 1

318 RERAISE 0
320 COPY 3
322 POP_EXCEPT
324 RERAISE 1


0 RETURN_GENERATOR
2 POP_TOP

4 LOAD_GLOBAL 1 (NULL + log_automation_step)
6 LOAD_FAST 0 (self)
8 LOAD_ATTR 1 (logger)
10 LOAD_CONST 1 ("CLEANUP")
12 LOAD_CONST 2 ("START")
14 CALL 3
16 POP_TOP

18 BUILD_LIST 0
20 STORE_FAST 1 (errors)

22 NOP

24 LOAD_FAST 0 (self)
26 LOAD_ATTR 2 (context)
28 POP_JUMP_FORWARD_IF_FALSE 135 (to 114)

30 LOAD_FAST 0 (self)
32 LOAD_METHOD 3 (get_default_pw_state_path)
34 CALL 0
36 STORE_FAST 2 (state_path_str)

38 NOP

40 LOAD_GLOBAL 9 (NULL + os)
42 LOAD_ATTR 5 (makedirs)
44 LOAD_GLOBAL 8 (os)
46 LOAD_ATTR 6 (path)
48 LOAD_METHOD 7 (dirname)
50 LOAD_FAST 2 (state_path_str)
52 CALL 1
54 LOAD_CONST 3 (True)
56 KW_NAMES 4 (('exist_ok',))
58 CALL 2
60 POP_TOP
62 JUMP_FORWARD 16 (to 86)
64 PUSH_EXC_INFO

66 LOAD_GLOBAL 16 (Exception)
68 CHECK_EXC_MATCH
70 POP_JUMP_FORWARD_IF_FALSE 3 (to 78)
72 POP_TOP

74 POP_EXCEPT
76 JUMP_FORWARD 4 (to 86)

78 RERAISE 0
80 COPY 3
82 POP_EXCEPT
84 RERAISE 1

86 LOAD_FAST 0 (self)
88 LOAD_ATTR 2 (context)
90 LOAD_METHOD 9 (storage_state)
92 LOAD_GLOBAL 21 (NULL + str)
94 LOAD_FAST 2 (state_path_str)
96 CALL 1
98 KW_NAMES 5 (('path',))
100 CALL 1
102 GET_AWAITABLE 0
104 LOAD_CONST 6 (None)
106 SEND 3 (to 112)
108 YIELD_VALUE
110 JUMP_BACKWARD_NO_INTERRUPT 4 (to 106)
112 POP_TOP
114 JUMP_FORWARD 47 (to 168)
116 PUSH_EXC_INFO

118 LOAD_GLOBAL 16 (Exception)
120 CHECK_EXC_MATCH
122 POP_JUMP_FORWARD_IF_FALSE 34 (to 160)
124 STORE_FAST 3 (e)

126 LOAD_FAST 1 (errors)
128 LOAD_METHOD 11 (append)
130 LOAD_CONST 7 ("storage_state: ")
132 LOAD_FAST 3 (e)
134 FORMAT_VALUE 0
136 BUILD_STRING 2
138 CALL 1
140 POP_TOP
142 POP_EXCEPT
144 LOAD_CONST 6 (None)
146 STORE_FAST 3 (e)
148 DELETE_FAST 3 (e)
150 JUMP_FORWARD 8 (to 168)
152 LOAD_CONST 6 (None)
154 STORE_FAST 3 (e)
156 DELETE_FAST 3 (e)
158 RERAISE 1

160 RERAISE 0
162 COPY 3
164 POP_EXCEPT
166 RERAISE 1

168 NOP

170 LOAD_FAST 0 (self)
172 LOAD_ATTR 12 (page)
174 POP_JUMP_FORWARD_IF_FALSE 105 (to 262)

176 NOP

178 LOAD_FAST 0 (self)
180 LOAD_ATTR 12 (page)
182 LOAD_METHOD 13 (is_closed)
184 CALL 0
186 POP_JUMP_FORWARD_IF_TRUE 31 (to 208)

188 LOAD_FAST 0 (self)
190 LOAD_ATTR 12 (page)
192 LOAD_METHOD 14 (close)
194 CALL 0
196 GET_AWAITABLE 0
198 LOAD_CONST 6 (None)
200 SEND 3 (to 206)
202 YIELD_VALUE
204 JUMP_BACKWARD_NO_INTERRUPT 4 (to 200)
206 POP_TOP
208 JUMP_FORWARD 47 (to 262)
210 PUSH_EXC_INFO

212 LOAD_GLOBAL 16 (Exception)
214 CHECK_EXC_MATCH
216 POP_JUMP_FORWARD_IF_FALSE 34 (to 254)
218 STORE_FAST 3 (e)

220 LOAD_FAST 1 (errors)
222 LOAD_METHOD 11 (append)
224 LOAD_CONST 8 ("page.close: ")
226 LOAD_FAST 3 (e)
228 FORMAT_VALUE 0
230 BUILD_STRING 2
232 CALL 1
234 POP_TOP
236 POP_EXCEPT
238 LOAD_CONST 6 (None)
240 STORE_FAST 3 (e)
242 DELETE_FAST 3 (e)
244 JUMP_FORWARD 8 (to 262)
246 LOAD_CONST 6 (None)
248 STORE_FAST 3 (e)
250 DELETE_FAST 3 (e)
252 RERAISE 1

254 RERAISE 0
256 COPY 3
258 POP_EXCEPT
260 RERAISE 1
262 JUMP_FORWARD 47 (to 316)
264 PUSH_EXC_INFO

266 LOAD_GLOBAL 16 (Exception)
268 CHECK_EXC_MATCH
270 POP_JUMP_FORWARD_IF_FALSE 34 (to 308)
272 STORE_FAST 3 (e)

274 LOAD_FAST 1 (errors)
276 LOAD_METHOD 11 (append)
278 LOAD_CONST 9 ("page.check: ")
280 LOAD_FAST 3 (e)
282 FORMAT_VALUE 0
284 BUILD_STRING 2
286 CALL 1
288 POP_TOP
290 POP_EXCEPT
292 LOAD_CONST 6 (None)
294 STORE_FAST 3 (e)
296 DELETE_FAST 3 (e)
298 JUMP_FORWARD 8 (to 316)
300 LOAD_CONST 6 (None)
302 STORE_FAST 3 (e)
304 DELETE_FAST 3 (e)
306 RERAISE 1

308 RERAISE 0
310 COPY 3
312 POP_EXCEPT
314 RERAISE 1

316 NOP

318 LOAD_FAST 0 (self)
320 LOAD_ATTR 2 (context)
322 POP_JUMP_FORWARD_IF_FALSE 80 (to 400)

324 NOP

326 LOAD_FAST 0 (self)
328 LOAD_ATTR 2 (context)
330 LOAD_METHOD 14 (close)
332 CALL 0
334 GET_AWAITABLE 0
336 LOAD_CONST 6 (None)
338 SEND 3 (to 344)
340 YIELD_VALUE
342 JUMP_BACKWARD_NO_INTERRUPT 4 (to 338)
344 POP_TOP
346 JUMP_FORWARD 47 (to 400)
348 PUSH_EXC_INFO

350 LOAD_GLOBAL 16 (Exception)
352 CHECK_EXC_MATCH
354 POP_JUMP_FORWARD_IF_FALSE 34 (to 392)
356 STORE_FAST 3 (e)

358 LOAD_FAST 1 (errors)
360 LOAD_METHOD 11 (append)
362 LOAD_CONST 10 ("context.close: ")
364 LOAD_FAST 3 (e)
366 FORMAT_VALUE 0
368 BUILD_STRING 2
370 CALL 1
372 POP_TOP
374 POP_EXCEPT
376 LOAD_CONST 6 (None)
378 STORE_FAST 3 (e)
380 DELETE_FAST 3 (e)
382 JUMP_FORWARD 8 (to 400)
384 LOAD_CONST 6 (None)
386 STORE_FAST 3 (e)
388 DELETE_FAST 3 (e)
390 RERAISE 1

392 RERAISE 0
394 COPY 3
396 POP_EXCEPT
398 RERAISE 1
400 JUMP_FORWARD 47 (to 454)
402 PUSH_EXC_INFO

404 LOAD_GLOBAL 16 (Exception)
406 CHECK_EXC_MATCH
408 POP_JUMP_FORWARD_IF_FALSE 34 (to 446)
410 STORE_FAST 3 (e)

412 LOAD_FAST 1 (errors)
414 LOAD_METHOD 11 (append)
416 LOAD_CONST 11 ("context.check: ")
418 LOAD_FAST 3 (e)
420 FORMAT_VALUE 0
422 BUILD_STRING 2
424 CALL 1
426 POP_TOP
428 POP_EXCEPT
430 LOAD_CONST 6 (None)
432 STORE_FAST 3 (e)
434 DELETE_FAST 3 (e)
436 JUMP_FORWARD 8 (to 454)
438 LOAD_CONST 6 (None)
440 STORE_FAST 3 (e)
442 DELETE_FAST 3 (e)
444 RERAISE 1

446 RERAISE 0
448 COPY 3
450 POP_EXCEPT
452 RERAISE 1

454 NOP

456 LOAD_FAST 0 (self)
458 LOAD_ATTR 15 (browser)
460 POP_JUMP_FORWARD_IF_FALSE 80 (to 538)

462 NOP

464 LOAD_FAST 0 (self)
466 LOAD_ATTR 15 (browser)
468 LOAD_METHOD 14 (close)
470 CALL 0
472 GET_AWAITABLE 0
474 LOAD_CONST 6 (None)
476 SEND 3 (to 482)
478 YIELD_VALUE
480 JUMP_BACKWARD_NO_INTERRUPT 4 (to 476)
482 POP_TOP
484 JUMP_FORWARD 47 (to 538)
486 PUSH_EXC_INFO

488 LOAD_GLOBAL 16 (Exception)
490 CHECK_EXC_MATCH
492 POP_JUMP_FORWARD_IF_FALSE 34 (to 530)
494 STORE_FAST 3 (e)

496 LOAD_FAST 1 (errors)
498 LOAD_METHOD 11 (append)
500 LOAD_CONST 12 ("browser.close: ")
502 LOAD_FAST 3 (e)
504 FORMAT_VALUE 0
506 BUILD_STRING 2
508 CALL 1
510 POP_TOP
512 POP_EXCEPT
514 LOAD_CONST 6 (None)
516 STORE_FAST 3 (e)
518 DELETE_FAST 3 (e)
520 JUMP_FORWARD 8 (to 538)
522 LOAD_CONST 6 (None)
524 STORE_FAST 3 (e)
526 DELETE_FAST 3 (e)
528 RERAISE 1

530 RERAISE 0
532 COPY 3
534 POP_EXCEPT
536 RERAISE 1
538 JUMP_FORWARD 47 (to 592)
540 PUSH_EXC_INFO

542 LOAD_GLOBAL 16 (Exception)
544 CHECK_EXC_MATCH
546 POP_JUMP_FORWARD_IF_FALSE 34 (to 584)
548 STORE_FAST 3 (e)

550 LOAD_FAST 1 (errors)
552 LOAD_METHOD 11 (append)
554 LOAD_CONST 13 ("browser.check: ")
556 LOAD_FAST 3 (e)
558 FORMAT_VALUE 0
560 BUILD_STRING 2
562 CALL 1
564 POP_TOP
566 POP_EXCEPT
568 LOAD_CONST 6 (None)
570 STORE_FAST 3 (e)
572 DELETE_FAST 3 (e)
574 JUMP_FORWARD 8 (to 592)
576 LOAD_CONST 6 (None)
578 STORE_FAST 3 (e)
580 DELETE_FAST 3 (e)
582 RERAISE 1

584 RERAISE 0
586 COPY 3
588 POP_EXCEPT
590 RERAISE 1

592 LOAD_FAST 1 (errors)
594 POP_JUMP_FORWARD_IF_FALSE 35 (to 628)

596 LOAD_GLOBAL 1 (NULL + log_automation_step)
598 LOAD_FAST 0 (self)
600 LOAD_ATTR 1 (logger)
602 LOAD_CONST 1 ("CLEANUP")
604 LOAD_CONST 14 ("PARTIAL")
606 LOAD_CONST 15 ("details")
608 LOAD_FAST 1 (errors)
610 LOAD_CONST 6 (None)
612 LOAD_CONST 16 (5)
614 BUILD_SLICE 2
616 BINARY_SUBSCR
618 BUILD_MAP 1
620 CALL 4
622 POP_TOP
624 LOAD_CONST 6 (None)
626 RETURN_VALUE

628 LOAD_GLOBAL 1 (NULL + log_automation_step)
630 LOAD_FAST 0 (self)
632 LOAD_ATTR 1 (logger)
634 LOAD_CONST 1 ("CLEANUP")
636 LOAD_CONST 17 ("SUCCESS")
638 CALL 3
640 POP_TOP
642 LOAD_CONST 6 (None)
644 RETURN_VALUE