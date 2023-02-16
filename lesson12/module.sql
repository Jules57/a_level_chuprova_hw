--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Homebrew)
-- Dumped by pg_dump version 14.6 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: module_table; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.module_table (
    id integer NOT NULL,
    name character varying(50),
    pwd character varying(128),
    email character varying(128),
    gender character varying(1)
);


ALTER TABLE public.module_table OWNER TO julia;

--
-- Name: module_table_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.module_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.module_table_id_seq OWNER TO julia;

--
-- Name: module_table_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.module_table_id_seq OWNED BY public.module_table.id;


--
-- Name: vocabulary; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.vocabulary (
    id integer NOT NULL,
    name character varying(255),
    info text
);


ALTER TABLE public.vocabulary OWNER TO julia;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.vocabulary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vocabulary_id_seq OWNER TO julia;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.vocabulary_id_seq OWNED BY public.vocabulary.id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.word (
    id integer NOT NULL,
    word character varying(255),
    vocabulary_id integer
);


ALTER TABLE public.word OWNER TO julia;

--
-- Name: word_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.word_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.word_id_seq OWNER TO julia;

--
-- Name: word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.word_id_seq OWNED BY public.word.id;


--
-- Name: module_table id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.module_table ALTER COLUMN id SET DEFAULT nextval('public.module_table_id_seq'::regclass);


--
-- Name: vocabulary id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.vocabulary ALTER COLUMN id SET DEFAULT nextval('public.vocabulary_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: module_table; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.module_table (id, name, pwd, email, gender) FROM stdin;
1	Vasya	21341234qwfsdf	mmm@mmail.com	m
2	Alex	21341234	mmm@gmail.com	m
3	Alexey	qq21341234Q	alexey@gmail.com	m
4	Helen	MarryMeee	hell@gmail.com	f
5	Jenny	SmakeMyb	eachup@gmail.com	f
6	Lora	burn23	tpicks@gmail.com	f
\.


--
-- Data for Name: vocabulary; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.vocabulary (id, name, info) FROM stdin;
1	animals	\N
2	school	\N
3	nature	\N
4	human	\N
5	SF	\N
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.word (id, word, vocabulary_id) FROM stdin;
1	turtle	1
2	pig	1
3	dog	1
4	cat	1
5	lizard	1
6	cow	1
7	rabbit	1
8	frog	1
9	headgehog	1
10	goat	1
11	desk	2
12	book	2
13	chalk	2
14	pen	2
15	pencil	2
16	copybook	2
17	lesson	2
18	teacher	2
19	pupils	2
20	school	2
21	ray	3
22	thunder	3
23	sun	3
24	field	3
25	hill	3
26	mountain	3
27	river	3
28	forest	3
29	grass	3
30	rain	3
31	hair	4
32	nail	4
33	finger	4
34	eye	4
35	tooth	4
36	knee	4
37	elbow	4
38	leg	4
39	arm	4
40	head	4
41	engine	5
42	steel	5
43	power	5
44	nuclear	5
45	shotgun	5
46	laser	5
47	flight	5
48	energy	5
49	Moon	5
50	splace	5
\.


--
-- Name: module_table_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.module_table_id_seq', 1, false);


--
-- Name: vocabulary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.vocabulary_id_seq', 5, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.word_id_seq', 50, true);


--
-- PostgreSQL database dump complete
--

