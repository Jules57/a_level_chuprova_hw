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
-- Name: actors; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    actor_lname character varying(50),
    actor_fname character varying(50),
    birth_date date,
    director_id integer,
    film_id integer
);


ALTER TABLE public.actors OWNER TO julia;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_actor_id_seq OWNER TO julia;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;


--
-- Name: actors_to_films; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.actors_to_films (
    act_id integer,
    film_id integer
);


ALTER TABLE public.actors_to_films OWNER TO julia;

--
-- Name: authors; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.authors (
    id integer NOT NULL,
    name character varying(200) DEFAULT 'lore'::character varying NOT NULL,
    year date DEFAULT '1970-01-01'::date NOT NULL
);


ALTER TABLE public.authors OWNER TO julia;

--
-- Name: authors_books; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.authors_books (
    author_id integer DEFAULT 0 NOT NULL,
    book_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.authors_books OWNER TO julia;

--
-- Name: authors_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.authors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authors_id_seq OWNER TO julia;

--
-- Name: authors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.authors_id_seq OWNED BY public.authors.id;


--
-- Name: books; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.books (
    id integer NOT NULL,
    title character varying(200) DEFAULT 'noname'::character varying NOT NULL,
    genre_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.books OWNER TO julia;

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO julia;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_lname character varying(128) NOT NULL,
    director_fname character varying(128) NOT NULL,
    birth_date date NOT NULL,
    film_amount integer,
    film_id integer NOT NULL,
    actor_id integer NOT NULL
);


ALTER TABLE public.directors OWNER TO julia;

--
-- Name: directors_director_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.directors_director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_director_id_seq OWNER TO julia;

--
-- Name: directors_director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.directors_director_id_seq OWNED BY public.directors.director_id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.films (
    film_id integer NOT NULL,
    film_name character varying(128),
    director_lname character varying(50),
    director_fname character varying(50),
    release_year integer,
    imdb numeric,
    director_id integer,
    actor_id integer
);


ALTER TABLE public.films OWNER TO julia;

--
-- Name: films_film_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.films_film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_film_id_seq OWNER TO julia;

--
-- Name: films_film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.films_film_id_seq OWNED BY public.films.film_id;


--
-- Name: genres; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.genres (
    id integer NOT NULL,
    genre character varying(100) DEFAULT 'unknown'::character varying NOT NULL
);


ALTER TABLE public.genres OWNER TO julia;

--
-- Name: genres_id_seq; Type: SEQUENCE; Schema: public; Owner: julia
--

CREATE SEQUENCE public.genres_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genres_id_seq OWNER TO julia;

--
-- Name: genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: julia
--

ALTER SEQUENCE public.genres_id_seq OWNED BY public.genres.id;


--
-- Name: word; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.word (
    id integer NOT NULL,
    word character varying(50),
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
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: authors id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.authors ALTER COLUMN id SET DEFAULT nextval('public.authors_id_seq'::regclass);


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: directors director_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.directors ALTER COLUMN director_id SET DEFAULT nextval('public.directors_director_id_seq'::regclass);


--
-- Name: films film_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.films ALTER COLUMN film_id SET DEFAULT nextval('public.films_film_id_seq'::regclass);


--
-- Name: genres id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.genres ALTER COLUMN id SET DEFAULT nextval('public.genres_id_seq'::regclass);


--
-- Name: word id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.word ALTER COLUMN id SET DEFAULT nextval('public.word_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.actors (actor_id, actor_lname, actor_fname, birth_date, director_id, film_id) FROM stdin;
8	Statham	Jason	1967-07-26	2	2
4	DiCaprio	Leonardo	1974-11-11	3	4
2	Pitt	Brad	1963-12-18	7	9
5	Radcliffe	Daniel	1989-07-23	8	10
3	Tennant	David	1971-04-18	6	8
1	Farrell	Colin	1976-05-31	4	6
\.


--
-- Data for Name: actors_to_films; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.actors_to_films (act_id, film_id) FROM stdin;
2	9
5	10
8	2
8	1
1	6
3	8
1	3
4	4
4	5
\.


--
-- Data for Name: authors; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.authors (id, name, year) FROM stdin;
1	Frank Herbert	1970-01-01
2	Michael Bulgakov	1970-01-01
3	Jack London	1970-01-01
4	Johann Goethe	1970-01-01
5	Robert Heinlein	1970-01-01
\.


--
-- Data for Name: authors_books; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.authors_books (author_id, book_id) FROM stdin;
1	4
2	1
3	3
4	2
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.books (id, title, genre_id) FROM stdin;
1	Master and Margo	2
2	Faust	0
3	White Fang	3
4	Dune	1
5	War and Piece	2
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.directors (director_id, director_lname, director_fname, birth_date, film_amount, film_id, actor_id) FROM stdin;
2	Ritchie	Guy	1968-10-09	14	1	1
3	Nolan	Christopher	1970-07-30	12	3	4
4	McDonagh	Martin	1970-03-26	5	6	1
5	Hitchcock	Alfred	1899-08-13	36	7	3
6	Mullan	Robert	1980-08-15	3	8	3
7	Leitch	David	1975-11-16	8	9	2
8	Scheinert	Daniel	1988-02-10	3	10	5
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.films (film_id, film_name, director_lname, director_fname, release_year, imdb, director_id, actor_id) FROM stdin;
1	Wrath of Man	Ritchie	Guy	2021	7.1	2	8
2	Revolver	Ritchie	Guy	2005	6.3	2	8
4	Inception	Nolan	Christopher	2010	8.8	3	4
3	Sherlock Holmes	Ritchie	Guy	2009	7.6	2	1
5	The Prestige	Nolan	Chirstopher	2006	8.5	3	1
6	Seven Psychopaths	McDonagh	Martin	2012	7.1	4	1
7	Psycho	Hitchcock	Alfred	1960	8.5	5	1
8	Mad to Be Normal	Mullan	Robert	2017	6.2	6	3
9	Bullet Train	Leitch	David	2022	7.8	7	2
10	Swiss Army Man	Scheinert	Daniel	2016	8.2	8	5
\.


--
-- Data for Name: genres; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.genres (id, genre) FROM stdin;
1	SF
2	novel
3	story
4	horror
\.


--
-- Data for Name: word; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.word (id, word, vocabulary_id) FROM stdin;
1	cat	1
2	dog	1
3	donkey	1
4	horse	1
5	badger	1
6	cow	1
7	API	2
8	CSS	2
9	HTML	2
10	CRUD	2
11	JSON	2
12	HTTP	2
13	REST	2
14	ORM	2
15	TDD	2
\.


--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 8, true);


--
-- Name: authors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.authors_id_seq', 5, true);


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.books_id_seq', 5, true);


--
-- Name: directors_director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.directors_director_id_seq', 8, true);


--
-- Name: films_film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.films_film_id_seq', 10, true);


--
-- Name: genres_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.genres_id_seq', 4, true);


--
-- Name: word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.word_id_seq', 15, true);


--
-- Name: authors authors_pkey; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (director_id);


--
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);


--
-- Name: actors unique_actor; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT unique_actor UNIQUE (actor_id);


--
-- Name: films unique_film; Type: CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT unique_film UNIQUE (film_id);


--
-- Name: directors directors_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);


--
-- Name: directors directors_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.films(film_id);


--
-- Name: actors fk_actors_directors; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT fk_actors_directors FOREIGN KEY (director_id) REFERENCES public.directors(director_id);


--
-- Name: actors fk_actors_films; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT fk_actors_films FOREIGN KEY (film_id) REFERENCES public.films(film_id);


--
-- Name: films fk_films_actors; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT fk_films_actors FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);


--
-- Name: films fk_films_directors; Type: FK CONSTRAINT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT fk_films_directors FOREIGN KEY (director_id) REFERENCES public.directors(director_id);


--
-- PostgreSQL database dump complete
--

