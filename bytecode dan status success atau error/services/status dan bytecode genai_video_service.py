Python Code - Decompilation Success


0 LOAD_CONST 0 ("\nGenAI Video Service: wrapper modular untuk Google Gen AI (Gemini API) video generation.\nMenggunakan package `google-genai`.\n\nReferensi:\n- https://ai.google.dev/gemini-api/docs/video\n- https://googleapis.github.io/python-genai/\n")
2 STORE_NAME 0 (__doc__)

4 LOAD_CONST 1 (0)
6 LOAD_CONST 2 (('annotations',))
8 IMPORT_NAME 1 (__future__)
10 IMPORT_FROM 2 (annotations)
12 STORE_NAME 2 (annotations)
14 POP_TOP

16 LOAD_CONST 1 (0)
18 LOAD_CONST 3 (None)
20 IMPORT_NAME 3 (time)
22 STORE_NAME 3 (time)

24 LOAD_CONST 1 (0)
26 LOAD_CONST 4 (('Optional', 'Dict', 'Any'))
28 IMPORT_NAME 4 (typing)
30 IMPORT_FROM 5 (Optional)
32 STORE_NAME 5 (Optional)
34 IMPORT_FROM 6 (Dict)
36 STORE_NAME 6 (Dict)
38 IMPORT_FROM 7 (Any)
40 STORE_NAME 7 (Any)
42 POP_TOP

44 LOAD_CONST 1 (0)
46 LOAD_CONST 5 (('genai',))
48 IMPORT_NAME 8 (google)
50 IMPORT_FROM 9 (genai)
52 STORE_NAME 9 (genai)
54 POP_TOP

56 LOAD_CONST 1 (0)
58 LOAD_CONST 6 (('types',))
60 IMPORT_NAME 10 (google.genai)
62 IMPORT_FROM 11 (types)
64 STORE_NAME 11 (types)
66 POP_TOP

68 PUSH_NULL
70 LOAD_BUILD_CLASS
72 LOAD_CONST 7 (code object GenAIVideoService)
74 MAKE_FUNCTION 0 (No arguments)
76 LOAD_CONST 8 ("GenAIVideoService")
78 CALL 2
80 STORE_NAME 12 (GenAIVideoService)
82 LOAD_CONST 3 (None)
84 RETURN_VALUE


0 LOAD_NAME 0 (__name__)
2 STORE_NAME 1 (__module__)
4 LOAD_CONST 0 ("GenAIVideoService")
6 STORE_NAME 2 (__qualname__)

8 LOAD_CONST 1 ("Service pembungkus untuk operasi video/image melalui Google Gen AI SDK.\n\n    Catatan API Key:\n    - API key dioper dari GUI dan dibangun ke Client langsung via parameter `api_key`.\n    ")
10 STORE_NAME 3 (__doc__)

12 LOAD_CONST 33 ((None,))
14 LOAD_CONST 34 (('api_key', 'Optional[str]'))
16 LOAD_CONST 5 (code object __init__)
18 MAKE_FUNCTION 5 (default, annotation)
20 STORE_NAME 4 (__init__)

22 LOAD_CONST 35 (('imagen-4.0-generate-001',))
24 LOAD_CONST 36 (('prompt', 'str', 'imagen_model', 'str', 'return', 'Any'))
26 LOAD_CONST 12 (code object generate_image_with_imagen)
28 MAKE_FUNCTION 5 (default, annotation)
30 STORE_NAME 5 (generate_image_with_imagen)

32 LOAD_CONST 13 ("veo-3.0-generate-001")
34 LOAD_CONST 2 (None)

36 LOAD_CONST 2 (None)

38 LOAD_CONST 2 (None)

40 LOAD_CONST 2 (None)

42 LOAD_CONST 14 (10)

44 LOAD_CONST 15 (('model', 'aspect_ratio', 'negative_prompt', 'image', 'resolution', 'poll_interval'))
46 BUILD_CONST_KEY_MAP 6
48 LOAD_CONST 37 (('prompt', 'str', 'model', 'str', 'aspect_ratio', 'Optional[str]', 'negative_prompt', 'Optional[str]', 'image', 'Optional[Any]', 'resolution', 'Optional[str]', 'poll_interval', 'int', 'return', 'Dict[str, Any]'))
50 LOAD_CONST 25 (code object generate_video)
52 MAKE_FUNCTION 6 (keyword-only, annotation)
54 STORE_NAME 6 (generate_video)

56 LOAD_CONST 38 (('generated_video', 'Any', 'output_path', 'str', 'return', 'str'))
58 LOAD_CONST 28 (code object download_video)
60 MAKE_FUNCTION 4 (annotation)
62 STORE_NAME 7 (download_video)

64 LOAD_CONST 39 (('generated_videos', 'Any', 'output_paths', 'list[str]', 'return', 'list[str]'))
66 LOAD_CONST 32 (code object download_videos)
68 MAKE_FUNCTION 4 (annotation)
70 STORE_NAME 8 (download_videos)
72 LOAD_CONST 2 (None)
74 RETURN_VALUE


0 LOAD_FAST 1 (api_key)
2 POP_JUMP_FORWARD_IF_FALSE 66 (to 34)
4 LOAD_FAST 1 (api_key)
6 LOAD_METHOD 0 (strip)
8 CALL 0
10 POP_JUMP_FORWARD_IF_FALSE 46 (to 34)

12 LOAD_GLOBAL 3 (NULL + genai)
14 LOAD_ATTR 2 (Client)
16 LOAD_FAST 1 (api_key)
18 LOAD_METHOD 0 (strip)
20 CALL 0
22 KW_NAMES 1 (('api_key',))
24 CALL 1
26 LOAD_FAST 0 (self)
28 STORE_ATTR 3 (client)
30 LOAD_CONST 0 (None)
32 RETURN_VALUE

34 LOAD_GLOBAL 3 (NULL + genai)
36 LOAD_ATTR 2 (Client)
38 CALL 0
40 LOAD_FAST 0 (self)
42 STORE_ATTR 3 (client)
44 LOAD_CONST 0 (None)
46 RETURN_VALUE


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (client)
4 LOAD_ATTR 1 (models)
6 LOAD_METHOD 2 (generate_images)

8 LOAD_FAST 2 (imagen_model)

10 LOAD_FAST 1 (prompt)

12 KW_NAMES 1 (('model', 'prompt'))
14 CALL 2
16 STORE_FAST 3 (resp)

18 LOAD_GLOBAL 7 (NULL + getattr)
20 LOAD_FAST 3 (resp)
22 LOAD_CONST 2 ("generated_images")
24 LOAD_CONST 3 (None)
26 CALL 3
28 POP_JUMP_FORWARD_IF_TRUE 15 (to 38)

30 LOAD_GLOBAL 9 (NULL + RuntimeError)
32 LOAD_CONST 4 ("Imagen tidak mengembalikan gambar.")
34 CALL 1
36 RAISE_VARARGS 1 (exception instance)

38 LOAD_FAST 3 (resp)
40 LOAD_ATTR 5 (generated_images)
42 LOAD_CONST 5 (0)
44 BINARY_SUBSCR
46 LOAD_ATTR 6 (image)
48 RETURN_VALUE


0 LOAD_FAST 2 (model)

2 LOAD_FAST 1 (prompt)

4 LOAD_CONST 1 (('model', 'prompt'))
6 BUILD_CONST_KEY_MAP 2
8 STORE_FAST 8 (kwargs)

10 LOAD_FAST 5 (image)
12 POP_JUMP_FORWARD_IF_NONE 5 (to 22)

14 LOAD_FAST 5 (image)
16 LOAD_FAST 8 (kwargs)
18 LOAD_CONST 3 ("image")
20 STORE_SUBSCR

22 BUILD_MAP 0
24 STORE_FAST 9 (cfg_kwargs)

26 LOAD_FAST 4 (negative_prompt)
28 POP_JUMP_FORWARD_IF_FALSE 5 (to 38)

30 LOAD_FAST 4 (negative_prompt)
32 LOAD_FAST 9 (cfg_kwargs)
34 LOAD_CONST 4 ("negative_prompt")
36 STORE_SUBSCR

38 LOAD_FAST 3 (aspect_ratio)
40 POP_JUMP_FORWARD_IF_FALSE 5 (to 50)

42 LOAD_FAST 3 (aspect_ratio)
44 LOAD_FAST 9 (cfg_kwargs)
46 LOAD_CONST 5 ("aspect_ratio")
48 STORE_SUBSCR

50 LOAD_FAST 6 (resolution)
52 POP_JUMP_FORWARD_IF_FALSE 5 (to 62)

54 LOAD_FAST 6 (resolution)
56 LOAD_FAST 9 (cfg_kwargs)
58 LOAD_CONST 6 ("resolution")
60 STORE_SUBSCR

62 LOAD_FAST 9 (cfg_kwargs)
64 POP_JUMP_FORWARD_IF_FALSE 20 (to 86)

66 LOAD_GLOBAL 1 (NULL + types)
68 LOAD_ATTR 1 (GenerateVideosConfig)
70 LOAD_CONST 16 (())
72 BUILD_MAP 0
74 LOAD_FAST 9 (cfg_kwargs)
76 DICT_MERGE 1
78 CALL_FUNCTION_EX 1 (keyword and positional arguments)
80 LOAD_FAST 8 (kwargs)
82 LOAD_CONST 7 ("config")
84 STORE_SUBSCR

86 PUSH_NULL
88 LOAD_FAST 0 (self)
90 LOAD_ATTR 2 (client)
92 LOAD_ATTR 3 (models)
94 LOAD_ATTR 4 (generate_videos)
96 LOAD_CONST 16 (())
98 BUILD_MAP 0
100 LOAD_FAST 8 (kwargs)
102 DICT_MERGE 1
104 CALL_FUNCTION_EX 1 (keyword and positional arguments)
106 STORE_FAST 10 (operation)

108 LOAD_GLOBAL 11 (NULL + getattr)
110 LOAD_FAST 10 (operation)
112 LOAD_CONST 8 ("done")
114 LOAD_CONST 9 (False)
116 CALL 3
118 POP_JUMP_FORWARD_IF_TRUE 95 (to 166)

120 LOAD_GLOBAL 13 (NULL + time)
122 LOAD_ATTR 7 (sleep)
124 LOAD_GLOBAL 17 (NULL + max)
126 LOAD_CONST 10 (1)
128 LOAD_GLOBAL 19 (NULL + int)
130 LOAD_FAST 7 (poll_interval)
132 CALL 1
134 CALL 2
136 CALL 1
138 POP_TOP

140 LOAD_FAST 0 (self)
142 LOAD_ATTR 2 (client)
144 LOAD_ATTR 10 (operations)
146 LOAD_METHOD 11 (get)
148 LOAD_FAST 10 (operation)
150 CALL 1
152 STORE_FAST 10 (operation)

154 LOAD_GLOBAL 11 (NULL + getattr)
156 LOAD_FAST 10 (operation)
158 LOAD_CONST 8 ("done")
160 LOAD_CONST 9 (False)
162 CALL 3
164 POP_JUMP_BACKWARD_IF_FALSE 95 (to 120)

166 LOAD_GLOBAL 11 (NULL + getattr)
168 LOAD_FAST 10 (operation)
170 LOAD_CONST 11 ("response")
172 LOAD_CONST 2 (None)
174 CALL 3
176 POP_JUMP_FORWARD_IF_FALSE 22 (to 192)
178 LOAD_GLOBAL 11 (NULL + getattr)
180 LOAD_FAST 10 (operation)
182 LOAD_ATTR 12 (response)
184 LOAD_CONST 12 ("generated_videos")
186 LOAD_CONST 2 (None)
188 CALL 3
190 POP_JUMP_FORWARD_IF_TRUE 15 (to 200)

192 LOAD_GLOBAL 27 (NULL + RuntimeError)
194 LOAD_CONST 13 ("Operasi selesai tetapi tidak ada video yang dihasilkan.")
196 CALL 1
198 RAISE_VARARGS 1 (exception instance)

200 LOAD_FAST 10 (operation)

202 LOAD_FAST 10 (operation)
204 LOAD_ATTR 12 (response)
206 LOAD_ATTR 14 (generated_videos)
208 LOAD_CONST 14 (0)
210 BINARY_SUBSCR

212 LOAD_FAST 10 (operation)
214 LOAD_ATTR 12 (response)
216 LOAD_ATTR 14 (generated_videos)

218 LOAD_CONST 15 (('operation', 'generated_video', 'generated_videos'))
220 BUILD_CONST_KEY_MAP 3
222 RETURN_VALUE


0 LOAD_FAST 0 (self)
2 LOAD_ATTR 0 (client)
4 LOAD_ATTR 1 (files)
6 LOAD_METHOD 2 (download)
8 LOAD_FAST 1 (generated_video)
10 LOAD_ATTR 3 (video)
12 KW_NAMES 1 (('file',))
14 CALL 1
16 POP_TOP

18 LOAD_FAST 1 (generated_video)
20 LOAD_ATTR 3 (video)
22 LOAD_METHOD 4 (save)
24 LOAD_FAST 2 (output_path)
26 CALL 1
28 POP_TOP

30 LOAD_FAST 2 (output_path)
32 RETURN_VALUE


0 BUILD_LIST 0
2 STORE_FAST 3 (saved)

4 LOAD_GLOBAL 1 (NULL + enumerate)
6 LOAD_FAST 1 (generated_videos)
8 CALL 1
10 GET_ITER
12 FOR_ITER 122 (to 86)
14 UNPACK_SEQUENCE 2
16 STORE_FAST 4 (idx)
18 STORE_FAST 5 (gv)

20 LOAD_FAST 4 (idx)
22 LOAD_GLOBAL 3 (NULL + len)
24 LOAD_FAST 2 (output_paths)
26 CALL 1
28 COMPARE_OP 5 (>=)
30 POP_JUMP_FORWARD_IF_FALSE 2 (to 36)

32 POP_TOP
34 JUMP_FORWARD 97 (to 86)

36 LOAD_FAST 0 (self)
38 LOAD_ATTR 2 (client)
40 LOAD_ATTR 3 (files)
42 LOAD_METHOD 4 (download)
44 LOAD_FAST 5 (gv)
46 LOAD_ATTR 5 (video)
48 KW_NAMES 1 (('file',))
50 CALL 1
52 POP_TOP

54 LOAD_FAST 5 (gv)
56 LOAD_ATTR 5 (video)
58 LOAD_METHOD 6 (save)
60 LOAD_FAST 2 (output_paths)
62 LOAD_FAST 4 (idx)
64 BINARY_SUBSCR
66 CALL 1
68 POP_TOP

70 LOAD_FAST 3 (saved)
72 LOAD_METHOD 7 (append)
74 LOAD_FAST 2 (output_paths)
76 LOAD_FAST 4 (idx)
78 BINARY_SUBSCR
80 CALL 1
82 POP_TOP
84 JUMP_BACKWARD 123 (to 12)

86 LOAD_FAST 3 (saved)
88 RETURN_VALUE