Python Code - Decompilation Success



0 LOAD_CONST 0 ("\nLogs tab UI for Auto Cloud Skill.\nThis tab builds the Logs UI and binds necessary widgets/vars on the MainWindow (owner).\n")
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (None)
8 IMPORT_NAME 1 (tkinter)
10 STORE_NAME 2 (tk)

12 LOAD_CONST 1 (0)
14 LOAD_CONST 3 (('scrolledtext',))
16 IMPORT_NAME 1 (tkinter)
18 IMPORT_FROM 3 (scrolledtext)
20 STORE_NAME 3 (scrolledtext)
22 POP_TOP

24 LOAD_CONST 1 (0)
26 LOAD_CONST 2 (None)
28 IMPORT_NAME 4 (ttkbootstrap)
30 STORE_NAME 5 (ttk)

32 LOAD_CONST 1 (0)
34 LOAD_CONST 4 (('*',))
36 IMPORT_NAME 6 (ttkbootstrap.constants)
38 IMPORT_STAR

40 PUSH_NULL
42 LOAD_BUILD_CLASS
44 LOAD_CONST 5 (code object LogsTab)
46 MAKE_FUNCTION 0 (No arguments)
48 LOAD_CONST 6 ("LogsTab")
50 CALL 2
52 STORE_NAME 7 (LogsTab)
54 LOAD_CONST 2 (None)
56 RETURN_VALUE


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("LogsTab")
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
20 LOAD_CONST 3 ("Logs")
22 KW_NAMES 4 (('text',))
24 CALL 2
26 POP_TOP

28 LOAD_GLOBAL 7 (NULL + scrolledtext)
30 LOAD_ATTR 4 (ScrolledText)

32 LOAD_FAST 2 (frame)

34 LOAD_GLOBAL 10 (tk)
36 LOAD_ATTR 6 (WORD)

38 LOAD_CONST 5 (80)

40 LOAD_CONST 6 (25)

42 LOAD_CONST 7 (('Consolas', 9))

44 LOAD_CONST 8 ("#2b3e50")

46 LOAD_CONST 9 ("#ecf0f1")

48 LOAD_CONST 9 ("#ecf0f1")
50 KW_NAMES 10 (('wrap', 'width', 'height', 'font', 'bg', 'fg', 'insertbackground'))
52 CALL 8
54 LOAD_FAST 0 (self)
56 LOAD_ATTR 7 (owner)
58 STORE_ATTR 8 (log_text)

60 LOAD_FAST 0 (self)
62 LOAD_ATTR 7 (owner)
64 LOAD_ATTR 8 (log_text)
66 LOAD_METHOD 9 (pack)
68 LOAD_GLOBAL 20 (BOTH)
70 LOAD_CONST 11 (True)
72 KW_NAMES 12 (('fill', 'expand'))
74 CALL 2
76 POP_TOP

78 LOAD_GLOBAL 1 (NULL + ttk)
80 LOAD_ATTR 1 (Frame)
82 LOAD_FAST 2 (frame)
84 CALL 1
86 LOAD_FAST 0 (self)
88 LOAD_ATTR 7 (owner)
90 STORE_ATTR 11 (gmail_progress_container)

92 LOAD_GLOBAL 1 (NULL + ttk)
94 LOAD_ATTR 12 (Label)
96 LOAD_FAST 0 (self)
98 LOAD_ATTR 7 (owner)
100 LOAD_ATTR 11 (gmail_progress_container)
102 LOAD_CONST 13 ("")
104 LOAD_GLOBAL 26 (INFO)
106 KW_NAMES 14 (('text', 'bootstyle'))
108 CALL 3
110 LOAD_FAST 0 (self)
112 LOAD_ATTR 7 (owner)
114 STORE_ATTR 14 (gmail_progress_label)

116 LOAD_FAST 0 (self)
118 LOAD_ATTR 7 (owner)
120 LOAD_ATTR 14 (gmail_progress_label)
122 LOAD_METHOD 9 (pack)
124 LOAD_GLOBAL 30 (LEFT)
126 KW_NAMES 15 (('side',))
128 CALL 1
130 POP_TOP

132 LOAD_GLOBAL 1 (NULL + ttk)
134 LOAD_ATTR 16 (Progressbar)
136 LOAD_FAST 0 (self)
138 LOAD_ATTR 7 (owner)
140 LOAD_ATTR 11 (gmail_progress_container)
142 LOAD_CONST 16 ("horizontal")
144 LOAD_CONST 17 ("determinate")
146 LOAD_CONST 18 (250)
148 KW_NAMES 19 (('orient', 'mode', 'length'))
150 CALL 4
152 LOAD_FAST 0 (self)
154 LOAD_ATTR 7 (owner)
156 STORE_ATTR 17 (gmail_progress)

158 LOAD_FAST 0 (self)
160 LOAD_ATTR 7 (owner)
162 LOAD_ATTR 17 (gmail_progress)
164 LOAD_METHOD 9 (pack)
166 LOAD_GLOBAL 36 (RIGHT)
168 LOAD_CONST 20 ((10, 0))
170 KW_NAMES 21 (('side', 'padx'))
172 CALL 2
174 POP_TOP

176 LOAD_CONST 0 (None)
178 LOAD_FAST 0 (self)
180 LOAD_ATTR 7 (owner)
182 STORE_ATTR 19 (gmail_progress_job)

184 LOAD_CONST 22 (False)
186 LOAD_FAST 0 (self)
188 LOAD_ATTR 7 (owner)
190 STORE_ATTR 20 (gmail_progress_running)

192 LOAD_GLOBAL 1 (NULL + ttk)
194 LOAD_ATTR 1 (Frame)
196 LOAD_FAST 2 (frame)
198 CALL 1
200 STORE_FAST 3 (log_controls)

202 LOAD_FAST 3 (log_controls)
204 LOAD_METHOD 9 (pack)
206 LOAD_GLOBAL 42 (X)
208 LOAD_CONST 20 ((10, 0))
210 KW_NAMES 23 (('fill', 'pady'))
212 CALL 2
214 POP_TOP

216 LOAD_GLOBAL 1 (NULL + ttk)
218 LOAD_ATTR 22 (Button)

220 LOAD_FAST 3 (log_controls)

222 LOAD_CONST 24 ("Clear Logs")
224 LOAD_FAST 0 (self)
226 LOAD_ATTR 7 (owner)
228 LOAD_ATTR 23 (clear_logs)

230 LOAD_GLOBAL 48 (WARNING)

232 KW_NAMES 25 (('text', 'command', 'bootstyle'))
234 CALL 4

236 LOAD_METHOD 9 (pack)
238 LOAD_GLOBAL 30 (LEFT)
240 KW_NAMES 15 (('side',))
242 CALL 1
244 POP_TOP

246 LOAD_GLOBAL 1 (NULL + ttk)
248 LOAD_ATTR 22 (Button)

250 LOAD_FAST 3 (log_controls)

252 LOAD_CONST 26 ("Save Logs")
254 LOAD_FAST 0 (self)
256 LOAD_ATTR 7 (owner)
258 LOAD_ATTR 25 (save_logs)

260 LOAD_GLOBAL 26 (INFO)

262 KW_NAMES 25 (('text', 'command', 'bootstyle'))
264 CALL 4

266 LOAD_METHOD 9 (pack)
268 LOAD_GLOBAL 30 (LEFT)
270 LOAD_CONST 20 ((10, 0))
272 KW_NAMES 21 (('side', 'padx'))
274 CALL 2
276 POP_TOP
278 LOAD_CONST 0 (None)
280 RETURN_VALUE