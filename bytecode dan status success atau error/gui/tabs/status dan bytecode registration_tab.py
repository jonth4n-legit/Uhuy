<module>: Success: Equal

<module>.RegistrationTab: Success: Equal

<module>.RegistrationTab.__init__: Success: Equal

***<module>.RegistrationTab._build: Failure detected at line number 30 and instruction offset 190: Different bytecode




0 LOAD_CONST 0 ("\nRegistration tab UI for Auto Cloud Skill.\nThis tab builds the Registration Form and binds to variables/methods of MainWindow (owner).\n")
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (None)
8 IMPORT_NAME 1 (tkinter)
10 STORE_NAME 2 (tk)

12 LOAD_CONST 1 (0)
14 LOAD_CONST 2 (None)
16 IMPORT_NAME 3 (ttkbootstrap)
18 STORE_NAME 4 (ttk)

20 LOAD_CONST 1 (0)
22 LOAD_CONST 3 (('*',))
24 IMPORT_NAME 5 (ttkbootstrap.constants)
26 IMPORT_STAR

28 PUSH_NULL
30 LOAD_BUILD_CLASS
32 LOAD_CONST 4 (code object RegistrationTab)
34 MAKE_FUNCTION 0 (No arguments)
36 LOAD_CONST 5 ("RegistrationTab")
38 CALL 2
40 STORE_NAME 6 (RegistrationTab)
42 LOAD_CONST 2 (None)
44 RETURN_VALUE


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("RegistrationTab")
6 STORE_NAME 2 (__qualname__)

8 LOAD_CONST 1 (code object __init__)
10 MAKE_FUNCTION 0 (No arguments)
12 STORE_NAME 3 (__init__)

14 LOAD_CONST 2 (code object _build)
16 MAKE_FUNCTION 0 (No arguments)
18 STORE_NAME 4 (_build)
20 LOAD_CONST 3 (None)
22 RETURN_VALUE


0 LOAD_FAST 1 (owner)
2 LOAD_FAST 0 (self)
4 STORE_ATTR 0 (owner)

6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_build)
10 LOAD_FAST 2 (notebook)
12 CALL 1
14 POP_TOP
16 LOAD_CONST 0 (None)
18 RETURN_VALUE


0 LOAD_GLOBAL 1 (NULL + ttk)
2 LOAD_ATTR 1 (Frame)
4 LOAD_FAST 1 (notebook)
6 LOAD_CONST 1 (20)
8 KW_NAMES 2 (('padding',))
10 CALL 2
12 STORE_FAST 2 (frame)

14 LOAD_FAST 1 (notebook)
16 LOAD_METHOD 2 (add)
18 LOAD_FAST 2 (frame)
20 LOAD_CONST 3 ("Registration Form")
22 KW_NAMES 4 (('text',))
24 CALL 2
26 POP_TOP

28 LOAD_GLOBAL 1 (NULL + ttk)
30 LOAD_ATTR 3 (LabelFrame)
32 LOAD_FAST 2 (frame)
34 LOAD_CONST 5 ("Registration Data")
36 LOAD_CONST 6 (15)
38 KW_NAMES 7 (('text', 'padding'))
40 CALL 3
42 STORE_FAST 3 (form_frame)

44 LOAD_FAST 3 (form_frame)
46 LOAD_METHOD 4 (pack)
48 LOAD_GLOBAL 10 (BOTH)
50 LOAD_CONST 8 (True)
52 KW_NAMES 9 (('fill', 'expand'))
54 CALL 2
56 POP_TOP

58 LOAD_GLOBAL 1 (NULL + ttk)
60 LOAD_ATTR 6 (Label)
62 LOAD_FAST 3 (form_frame)
64 LOAD_CONST 10 ("First Name:")
66 KW_NAMES 4 (('text',))
68 CALL 2
70 LOAD_METHOD 7 (grid)
72 LOAD_CONST 11 (0)
74 LOAD_CONST 11 (0)
76 LOAD_GLOBAL 16 (W)
78 LOAD_CONST 12 (5)
80 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
82 CALL 4
84 POP_TOP

86 LOAD_GLOBAL 1 (NULL + ttk)
88 LOAD_ATTR 9 (Entry)

90 LOAD_FAST 3 (form_frame)

92 LOAD_FAST 0 (self)
94 LOAD_ATTR 10 (owner)
96 LOAD_ATTR 11 (first_name_var)

98 LOAD_CONST 14 (30)

100 KW_NAMES 15 (('textvariable', 'width'))
102 CALL 3
104 STORE_FAST 4 (first_name_entry)

106 LOAD_FAST 4 (first_name_entry)
108 LOAD_METHOD 7 (grid)
110 LOAD_CONST 11 (0)
112 LOAD_CONST 16 (1)
114 LOAD_GLOBAL 16 (W)
116 LOAD_GLOBAL 24 (E)
118 BINARY_OP 0
120 LOAD_CONST 17 ((10, 0))
122 LOAD_CONST 12 (5)
124 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
126 CALL 5
128 POP_TOP

130 LOAD_GLOBAL 1 (NULL + ttk)
132 LOAD_ATTR 6 (Label)
134 LOAD_FAST 3 (form_frame)
136 LOAD_CONST 19 ("Last Name:")
138 KW_NAMES 4 (('text',))
140 CALL 2
142 LOAD_METHOD 7 (grid)
144 LOAD_CONST 16 (1)
146 LOAD_CONST 11 (0)
148 LOAD_GLOBAL 16 (W)
150 LOAD_CONST 12 (5)
152 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
154 CALL 4
156 POP_TOP

158 LOAD_GLOBAL 1 (NULL + ttk)
160 LOAD_ATTR 9 (Entry)

162 LOAD_FAST 3 (form_frame)

164 LOAD_FAST 0 (self)
166 LOAD_ATTR 10 (owner)
168 LOAD_ATTR 13 (last_name_var)

170 LOAD_CONST 14 (30)

172 KW_NAMES 15 (('textvariable', 'width'))
174 CALL 3
176 STORE_FAST 5 (last_name_entry)

178 LOAD_FAST 5 (last_name_entry)
180 LOAD_METHOD 7 (grid)
182 LOAD_CONST 16 (1)
184 LOAD_CONST 16 (1)
186 LOAD_GLOBAL 16 (W)
188 LOAD_GLOBAL 24 (E)
190 BINARY_OP 0
192 LOAD_CONST 17 ((10, 0))
194 LOAD_CONST 12 (5)
196 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
198 CALL 5
200 POP_TOP

202 LOAD_GLOBAL 1 (NULL + ttk)
204 LOAD_ATTR 6 (Label)
206 LOAD_FAST 3 (form_frame)
208 LOAD_CONST 20 ("Email:")
210 KW_NAMES 4 (('text',))
212 CALL 2
214 LOAD_METHOD 7 (grid)
216 LOAD_CONST 21 (2)
218 LOAD_CONST 11 (0)
220 LOAD_GLOBAL 16 (W)
222 LOAD_CONST 12 (5)
224 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
226 CALL 4
228 POP_TOP

230 LOAD_GLOBAL 1 (NULL + ttk)
232 LOAD_ATTR 9 (Entry)

234 LOAD_FAST 3 (form_frame)

236 LOAD_FAST 0 (self)
238 LOAD_ATTR 10 (owner)
240 LOAD_ATTR 14 (email_var)

242 LOAD_CONST 14 (30)

244 KW_NAMES 15 (('textvariable', 'width'))
246 CALL 3
248 STORE_FAST 6 (email_entry)

250 LOAD_FAST 6 (email_entry)
252 LOAD_METHOD 7 (grid)
254 LOAD_CONST 21 (2)
256 LOAD_CONST 16 (1)
258 LOAD_GLOBAL 16 (W)
260 LOAD_GLOBAL 24 (E)
262 BINARY_OP 0
264 LOAD_CONST 17 ((10, 0))
266 LOAD_CONST 12 (5)
268 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
270 CALL 5
272 POP_TOP

274 LOAD_GLOBAL 1 (NULL + ttk)
276 LOAD_ATTR 6 (Label)
278 LOAD_FAST 3 (form_frame)
280 LOAD_CONST 22 ("Company:")
282 KW_NAMES 4 (('text',))
284 CALL 2
286 LOAD_METHOD 7 (grid)
288 LOAD_CONST 23 (3)
290 LOAD_CONST 11 (0)
292 LOAD_GLOBAL 16 (W)
294 LOAD_CONST 12 (5)
296 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
298 CALL 4
300 POP_TOP

302 LOAD_GLOBAL 1 (NULL + ttk)
304 LOAD_ATTR 9 (Entry)

306 LOAD_FAST 3 (form_frame)

308 LOAD_FAST 0 (self)
310 LOAD_ATTR 10 (owner)
312 LOAD_ATTR 15 (company_var)

314 LOAD_CONST 14 (30)

316 KW_NAMES 15 (('textvariable', 'width'))
318 CALL 3
320 STORE_FAST 7 (company_entry)

322 LOAD_FAST 7 (company_entry)
324 LOAD_METHOD 7 (grid)
326 LOAD_CONST 23 (3)
328 LOAD_CONST 16 (1)
330 LOAD_GLOBAL 16 (W)
332 LOAD_GLOBAL 24 (E)
334 BINARY_OP 0
336 LOAD_CONST 17 ((10, 0))
338 LOAD_CONST 12 (5)
340 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
342 CALL 5
344 POP_TOP

346 LOAD_GLOBAL 1 (NULL + ttk)
348 LOAD_ATTR 6 (Label)
350 LOAD_FAST 3 (form_frame)
352 LOAD_CONST 24 ("Password:")
354 KW_NAMES 4 (('text',))
356 CALL 2
358 LOAD_METHOD 7 (grid)
360 LOAD_CONST 25 (4)
362 LOAD_CONST 11 (0)
364 LOAD_GLOBAL 16 (W)
366 LOAD_CONST 12 (5)
368 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
370 CALL 4
372 POP_TOP

374 LOAD_GLOBAL 1 (NULL + ttk)
376 LOAD_ATTR 9 (Entry)

378 LOAD_FAST 3 (form_frame)

380 LOAD_FAST 0 (self)
382 LOAD_ATTR 10 (owner)
384 LOAD_ATTR 16 (password_var)

386 LOAD_CONST 26 ("*")
388 LOAD_CONST 14 (30)

390 KW_NAMES 27 (('textvariable', 'show', 'width'))
392 CALL 4
394 LOAD_FAST 0 (self)
396 LOAD_ATTR 10 (owner)
398 STORE_ATTR 17 (password_entry)

400 LOAD_FAST 0 (self)
402 LOAD_ATTR 10 (owner)
404 LOAD_ATTR 17 (password_entry)
406 LOAD_METHOD 7 (grid)
408 LOAD_CONST 25 (4)
410 LOAD_CONST 16 (1)
412 LOAD_GLOBAL 16 (W)
414 LOAD_GLOBAL 24 (E)
416 BINARY_OP 0
418 LOAD_CONST 17 ((10, 0))
420 LOAD_CONST 12 (5)
422 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
424 CALL 5
426 POP_TOP

428 LOAD_GLOBAL 1 (NULL + ttk)
430 LOAD_ATTR 18 (Checkbutton)

432 LOAD_FAST 3 (form_frame)

434 LOAD_CONST 28 ("Show")
436 LOAD_FAST 0 (self)
438 LOAD_ATTR 10 (owner)
440 LOAD_ATTR 19 (show_password_var)

442 LOAD_FAST 0 (self)
444 LOAD_ATTR 10 (owner)
446 LOAD_ATTR 20 (toggle_password_visibility)

448 LOAD_CONST 29 ("round-toggle")
450 KW_NAMES 30 (('text', 'variable', 'command', 'bootstyle'))
452 CALL 5
454 STORE_FAST 8 (show_pw_check)

456 LOAD_FAST 8 (show_pw_check)
458 LOAD_METHOD 7 (grid)
460 LOAD_CONST 25 (4)
462 LOAD_CONST 21 (2)
464 LOAD_CONST 17 ((10, 0))
466 LOAD_GLOBAL 16 (W)
468 KW_NAMES 31 (('row', 'column', 'padx', 'sticky'))
470 CALL 4
472 POP_TOP

474 LOAD_GLOBAL 1 (NULL + ttk)
476 LOAD_ATTR 21 (Button)

478 LOAD_FAST 3 (form_frame)

480 LOAD_CONST 32 ("Copy")
482 LOAD_FAST 0 (self)
484 LOAD_ATTR 10 (owner)
486 LOAD_ATTR 22 (copy_password)

488 LOAD_GLOBAL 46 (INFO)

490 LOAD_CONST 33 (8)

492 KW_NAMES 34 (('text', 'command', 'bootstyle', 'width'))
494 CALL 5
496 STORE_FAST 9 (copy_pw_btn)

498 LOAD_FAST 9 (copy_pw_btn)
500 LOAD_METHOD 7 (grid)
502 LOAD_CONST 25 (4)
504 LOAD_CONST 23 (3)
506 LOAD_CONST 17 ((10, 0))
508 LOAD_GLOBAL 16 (W)
510 KW_NAMES 31 (('row', 'column', 'padx', 'sticky'))
512 CALL 4
514 POP_TOP

516 LOAD_GLOBAL 1 (NULL + ttk)
518 LOAD_ATTR 6 (Label)
520 LOAD_FAST 3 (form_frame)
522 LOAD_CONST 35 ("Confirm Password:")
524 KW_NAMES 4 (('text',))
526 CALL 2
528 LOAD_METHOD 7 (grid)
530 LOAD_CONST 12 (5)
532 LOAD_CONST 11 (0)
534 LOAD_GLOBAL 16 (W)
536 LOAD_CONST 12 (5)
538 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
540 CALL 4
542 POP_TOP

544 LOAD_GLOBAL 1 (NULL + ttk)
546 LOAD_ATTR 9 (Entry)

548 LOAD_FAST 3 (form_frame)

550 LOAD_FAST 0 (self)
552 LOAD_ATTR 10 (owner)
554 LOAD_ATTR 24 (password_confirm_var)

556 LOAD_CONST 26 ("*")
558 LOAD_CONST 14 (30)

560 KW_NAMES 27 (('textvariable', 'show', 'width'))
562 CALL 4
564 LOAD_FAST 0 (self)
566 LOAD_ATTR 10 (owner)
568 STORE_ATTR 25 (password_confirm_entry)

570 LOAD_FAST 0 (self)
572 LOAD_ATTR 10 (owner)
574 LOAD_ATTR 25 (password_confirm_entry)
576 LOAD_METHOD 7 (grid)
578 LOAD_CONST 12 (5)
580 LOAD_CONST 16 (1)
582 LOAD_GLOBAL 16 (W)
584 LOAD_GLOBAL 24 (E)
586 BINARY_OP 0
588 LOAD_CONST 17 ((10, 0))
590 LOAD_CONST 12 (5)
592 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
594 CALL 5
596 POP_TOP

598 LOAD_FAST 3 (form_frame)
600 LOAD_METHOD 26 (columnconfigure)
602 LOAD_CONST 16 (1)
604 LOAD_CONST 16 (1)
606 KW_NAMES 36 (('weight',))
608 CALL 2
610 POP_TOP
612 LOAD_CONST 0 (None)
614 RETURN_VALUE












0 LOAD_CONST 0 ("\nRegistration tab UI for Auto Cloud Skill.\nThis tab builds the Registration Form and binds to variables/methods of MainWindow (owner).\n")
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (None)
8 IMPORT_NAME 1 (tkinter)
10 STORE_NAME 2 (tk)

12 LOAD_CONST 1 (0)
14 LOAD_CONST 2 (None)
16 IMPORT_NAME 3 (ttkbootstrap)
18 STORE_NAME 4 (ttk)

20 LOAD_CONST 1 (0)
22 LOAD_CONST 3 (('*',))
24 IMPORT_NAME 5 (ttkbootstrap.constants)
26 IMPORT_STAR

28 PUSH_NULL
30 LOAD_BUILD_CLASS
32 LOAD_CONST 4 (code object RegistrationTab)
34 MAKE_FUNCTION 0 (No arguments)
36 LOAD_CONST 5 ("RegistrationTab")
38 CALL 2
40 STORE_NAME 6 (RegistrationTab)
42 LOAD_CONST 2 (None)
44 RETURN_VALUE


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("RegistrationTab")
6 STORE_NAME 2 (__qualname__)

8 LOAD_CONST 1 (code object __init__)
10 MAKE_FUNCTION 0 (No arguments)
12 STORE_NAME 3 (__init__)

14 LOAD_CONST 2 (code object _build)
16 MAKE_FUNCTION 0 (No arguments)
18 STORE_NAME 4 (_build)
20 LOAD_CONST 3 (None)
22 RETURN_VALUE


0 LOAD_FAST 1 (owner)
2 LOAD_FAST 0 (self)
4 STORE_ATTR 0 (owner)

6 LOAD_FAST 0 (self)
8 LOAD_METHOD 1 (_build)
10 LOAD_FAST 2 (notebook)
12 CALL 1
14 POP_TOP
16 LOAD_CONST 0 (None)
18 RETURN_VALUE


0 LOAD_GLOBAL 1 (NULL + ttk)
2 LOAD_ATTR 1 (Frame)
4 LOAD_FAST 1 (notebook)
6 LOAD_CONST 1 (20)
8 KW_NAMES 2 (('padding',))
10 CALL 2
12 STORE_FAST 2 (frame)

14 LOAD_FAST 1 (notebook)
16 LOAD_METHOD 2 (add)
18 LOAD_FAST 2 (frame)
20 LOAD_CONST 3 ("Registration Form")
22 KW_NAMES 4 (('text',))
24 CALL 2
26 POP_TOP

28 LOAD_GLOBAL 1 (NULL + ttk)
30 LOAD_ATTR 3 (LabelFrame)
32 LOAD_FAST 2 (frame)
34 LOAD_CONST 5 ("Registration Data")
36 LOAD_CONST 6 (15)
38 KW_NAMES 7 (('text', 'padding'))
40 CALL 3
42 STORE_FAST 3 (form_frame)

44 LOAD_FAST 3 (form_frame)
46 LOAD_METHOD 4 (pack)
48 LOAD_GLOBAL 10 (BOTH)
50 LOAD_CONST 8 (True)
52 KW_NAMES 9 (('fill', 'expand'))
54 CALL 2
56 POP_TOP

58 LOAD_GLOBAL 1 (NULL + ttk)
60 LOAD_ATTR 6 (Label)
62 LOAD_FAST 3 (form_frame)
64 LOAD_CONST 10 ("First Name:")
66 KW_NAMES 4 (('text',))
68 CALL 2
70 LOAD_METHOD 7 (grid)
72 LOAD_CONST 11 (0)
74 LOAD_CONST 11 (0)
76 LOAD_GLOBAL 16 (W)
78 LOAD_CONST 12 (5)
80 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
82 CALL 4
84 POP_TOP

86 LOAD_GLOBAL 1 (NULL + ttk)
88 LOAD_ATTR 9 (Entry)
90 LOAD_FAST 3 (form_frame)
92 LOAD_FAST 0 (self)
94 LOAD_ATTR 10 (owner)
96 LOAD_ATTR 11 (first_name_var)
98 LOAD_CONST 14 (30)
100 KW_NAMES 15 (('textvariable', 'width'))
102 CALL 3
104 STORE_FAST 4 (first_name_entry)

106 LOAD_FAST 4 (first_name_entry)
108 LOAD_METHOD 7 (grid)
110 LOAD_CONST 11 (0)
112 LOAD_CONST 16 (1)
114 LOAD_GLOBAL 16 (W)
116 LOAD_GLOBAL 24 (E)
118 BINARY_OP 0
120 LOAD_CONST 17 ((10, 0))
122 LOAD_CONST 12 (5)
124 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
126 CALL 5
128 POP_TOP

130 LOAD_GLOBAL 1 (NULL + ttk)
132 LOAD_ATTR 6 (Label)
134 LOAD_FAST 3 (form_frame)
136 LOAD_CONST 19 ("Last Name:")
138 KW_NAMES 4 (('text',))
140 CALL 2
142 LOAD_METHOD 7 (grid)
144 LOAD_CONST 16 (1)
146 LOAD_CONST 11 (0)
148 LOAD_GLOBAL 16 (W)
150 LOAD_CONST 12 (5)
152 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
154 CALL 4
156 POP_TOP

158 LOAD_GLOBAL 1 (NULL + ttk)
160 LOAD_ATTR 9 (Entry)
162 LOAD_FAST 3 (form_frame)
164 LOAD_FAST 0 (self)
166 LOAD_ATTR 10 (owner)
168 LOAD_ATTR 13 (last_name_var)
170 LOAD_CONST 14 (30)
172 KW_NAMES 15 (('textvariable', 'width'))
174 CALL 3
176 STORE_FAST 5 (last_name_entry)

178 LOAD_FAST 5 (last_name_entry)
180 LOAD_METHOD 7 (grid)
182 LOAD_CONST 16 (1)
184 LOAD_CONST 16 (1)
186 LOAD_GLOBAL 16 (W)
188 LOAD_GLOBAL 24 (E)
190 BINARY_OP 5
192 LOAD_CONST 17 ((10, 0))
194 LOAD_CONST 12 (5)
196 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
198 CALL 5
200 POP_TOP

202 LOAD_GLOBAL 1 (NULL + ttk)
204 LOAD_ATTR 6 (Label)
206 LOAD_FAST 3 (form_frame)
208 LOAD_CONST 20 ("Email:")
210 KW_NAMES 4 (('text',))
212 CALL 2
214 LOAD_METHOD 7 (grid)
216 LOAD_CONST 21 (2)
218 LOAD_CONST 11 (0)
220 LOAD_GLOBAL 16 (W)
222 LOAD_CONST 12 (5)
224 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
226 CALL 4
228 POP_TOP

230 LOAD_GLOBAL 1 (NULL + ttk)
232 LOAD_ATTR 9 (Entry)
234 LOAD_FAST 3 (form_frame)
236 LOAD_FAST 0 (self)
238 LOAD_ATTR 10 (owner)
240 LOAD_ATTR 14 (email_var)
242 LOAD_CONST 14 (30)
244 KW_NAMES 15 (('textvariable', 'width'))
246 CALL 3
248 STORE_FAST 6 (email_entry)

250 LOAD_FAST 6 (email_entry)
252 LOAD_METHOD 7 (grid)
254 LOAD_CONST 21 (2)
256 LOAD_CONST 16 (1)
258 LOAD_GLOBAL 16 (W)
260 LOAD_GLOBAL 24 (E)
262 BINARY_OP 0
264 LOAD_CONST 17 ((10, 0))
266 LOAD_CONST 12 (5)
268 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
270 CALL 5
272 POP_TOP

274 LOAD_GLOBAL 1 (NULL + ttk)
276 LOAD_ATTR 6 (Label)
278 LOAD_FAST 3 (form_frame)
280 LOAD_CONST 22 ("Company:")
282 KW_NAMES 4 (('text',))
284 CALL 2
286 LOAD_METHOD 7 (grid)
288 LOAD_CONST 23 (3)
290 LOAD_CONST 11 (0)
292 LOAD_GLOBAL 16 (W)
294 LOAD_CONST 12 (5)
296 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
298 CALL 4
300 POP_TOP

302 LOAD_GLOBAL 1 (NULL + ttk)
304 LOAD_ATTR 9 (Entry)
306 LOAD_FAST 3 (form_frame)
308 LOAD_FAST 0 (self)
310 LOAD_ATTR 10 (owner)
312 LOAD_ATTR 15 (company_var)
314 LOAD_CONST 14 (30)
316 KW_NAMES 15 (('textvariable', 'width'))
318 CALL 3
320 STORE_FAST 7 (company_entry)

322 LOAD_FAST 7 (company_entry)
324 LOAD_METHOD 7 (grid)
326 LOAD_CONST 23 (3)
328 LOAD_CONST 16 (1)
330 LOAD_GLOBAL 16 (W)
332 LOAD_GLOBAL 24 (E)
334 BINARY_OP 0
336 LOAD_CONST 17 ((10, 0))
338 LOAD_CONST 12 (5)
340 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
342 CALL 5
344 POP_TOP

346 LOAD_GLOBAL 1 (NULL + ttk)
348 LOAD_ATTR 6 (Label)
350 LOAD_FAST 3 (form_frame)
352 LOAD_CONST 24 ("Password:")
354 KW_NAMES 4 (('text',))
356 CALL 2
358 LOAD_METHOD 7 (grid)
360 LOAD_CONST 25 (4)
362 LOAD_CONST 11 (0)
364 LOAD_GLOBAL 16 (W)
366 LOAD_CONST 12 (5)
368 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
370 CALL 4
372 POP_TOP

374 LOAD_GLOBAL 1 (NULL + ttk)
376 LOAD_ATTR 9 (Entry)
378 LOAD_FAST 3 (form_frame)
380 LOAD_FAST 0 (self)
382 LOAD_ATTR 10 (owner)
384 LOAD_ATTR 16 (password_var)
386 LOAD_CONST 26 ("*")
388 LOAD_CONST 14 (30)
390 KW_NAMES 27 (('textvariable', 'show', 'width'))
392 CALL 4
394 LOAD_FAST 0 (self)
396 LOAD_ATTR 10 (owner)
398 STORE_ATTR 17 (password_entry)

400 LOAD_FAST 0 (self)
402 LOAD_ATTR 10 (owner)
404 LOAD_ATTR 17 (password_entry)
406 LOAD_METHOD 7 (grid)
408 LOAD_CONST 25 (4)
410 LOAD_CONST 16 (1)
412 LOAD_GLOBAL 16 (W)
414 LOAD_GLOBAL 24 (E)
416 BINARY_OP 5
418 LOAD_CONST 17 ((10, 0))
420 LOAD_CONST 12 (5)
422 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
424 CALL 5
426 POP_TOP

428 LOAD_GLOBAL 1 (NULL + ttk)
430 LOAD_ATTR 18 (Checkbutton)
432 LOAD_FAST 3 (form_frame)
434 LOAD_CONST 28 ("Show")
436 LOAD_FAST 0 (self)
438 LOAD_ATTR 10 (owner)
440 LOAD_ATTR 19 (show_password_var)
442 LOAD_FAST 0 (self)
444 LOAD_ATTR 10 (owner)
446 LOAD_ATTR 20 (toggle_password_visibility)
448 LOAD_CONST 29 ("round-toggle")
450 KW_NAMES 30 (('text', 'variable', 'command', 'bootstyle'))
452 CALL 5
454 STORE_FAST 8 (show_pw_check)

456 LOAD_FAST 8 (show_pw_check)
458 LOAD_METHOD 7 (grid)
460 LOAD_CONST 25 (4)
462 LOAD_CONST 21 (2)
464 LOAD_CONST 17 ((10, 0))
466 LOAD_GLOBAL 16 (W)
468 KW_NAMES 31 (('row', 'column', 'padx', 'sticky'))
470 CALL 4
472 POP_TOP

474 LOAD_GLOBAL 1 (NULL + ttk)
476 LOAD_ATTR 21 (Button)
478 LOAD_FAST 3 (form_frame)
480 LOAD_CONST 32 ("Copy")
482 LOAD_FAST 0 (self)
484 LOAD_ATTR 10 (owner)
486 LOAD_ATTR 22 (copy_password)
488 LOAD_GLOBAL 46 (INFO)
490 LOAD_CONST 33 (8)
492 KW_NAMES 34 (('text', 'command', 'bootstyle', 'width'))
494 CALL 5
496 STORE_FAST 9 (copy_pw_btn)

498 LOAD_FAST 9 (copy_pw_btn)
500 LOAD_METHOD 7 (grid)
502 LOAD_CONST 25 (4)
504 LOAD_CONST 23 (3)
506 LOAD_CONST 17 ((10, 0))
508 LOAD_GLOBAL 16 (W)
510 KW_NAMES 31 (('row', 'column', 'padx', 'sticky'))
512 CALL 4
514 POP_TOP

516 LOAD_GLOBAL 1 (NULL + ttk)
518 LOAD_ATTR 6 (Label)
520 LOAD_FAST 3 (form_frame)
522 LOAD_CONST 35 ("Confirm Password:")
524 KW_NAMES 4 (('text',))
526 CALL 2
528 LOAD_METHOD 7 (grid)
530 LOAD_CONST 12 (5)
532 LOAD_CONST 11 (0)
534 LOAD_GLOBAL 16 (W)
536 LOAD_CONST 12 (5)
538 KW_NAMES 13 (('row', 'column', 'sticky', 'pady'))
540 CALL 4
542 POP_TOP

544 LOAD_GLOBAL 1 (NULL + ttk)
546 LOAD_ATTR 9 (Entry)
548 LOAD_FAST 3 (form_frame)
550 LOAD_FAST 0 (self)
552 LOAD_ATTR 10 (owner)
554 LOAD_ATTR 24 (password_confirm_var)
556 LOAD_CONST 26 ("*")
558 LOAD_CONST 14 (30)
560 KW_NAMES 27 (('textvariable', 'show', 'width'))
562 CALL 4
564 LOAD_FAST 0 (self)
566 LOAD_ATTR 10 (owner)
568 STORE_ATTR 25 (password_confirm_entry)

570 LOAD_FAST 0 (self)
572 LOAD_ATTR 10 (owner)
574 LOAD_ATTR 25 (password_confirm_entry)
576 LOAD_METHOD 7 (grid)
578 LOAD_CONST 12 (5)
580 LOAD_CONST 16 (1)
582 LOAD_GLOBAL 16 (W)
584 LOAD_GLOBAL 24 (E)
586 BINARY_OP 0
588 LOAD_CONST 17 ((10, 0))
590 LOAD_CONST 12 (5)
592 KW_NAMES 18 (('row', 'column', 'sticky', 'padx', 'pady'))
594 CALL 5
596 POP_TOP

598 LOAD_FAST 3 (form_frame)
600 LOAD_METHOD 26 (columnconfigure)
602 LOAD_CONST 16 (1)
604 LOAD_CONST 16 (1)
606 KW_NAMES 36 (('weight',))
608 CALL 2
610 POP_TOP
612 LOAD_CONST 0 (None)
614 RETURN_VALUE