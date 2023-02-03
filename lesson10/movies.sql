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
    birth_date date
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
-- Name: directors; Type: TABLE; Schema: public; Owner: julia
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_lname character varying(50),
    director_fname character varying(50),
    birth_date date,
    films_amount smallint
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
    imdb numeric
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
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: directors director_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.directors ALTER COLUMN director_id SET DEFAULT nextval('public.directors_director_id_seq'::regclass);


--
-- Name: films film_id; Type: DEFAULT; Schema: public; Owner: julia
--

ALTER TABLE ONLY public.films ALTER COLUMN film_id SET DEFAULT nextval('public.films_film_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.actors (actor_id, actor_lname, actor_fname, birth_date) FROM stdin;
1	Farrell	Colin	1976-05-31
2	Pitt	Brad	1963-12-18
3	Tennant	David	1971-04-18
4	DiCaprio	Leonardo	1974-11-11
5	Radcliffe	Daniel	1989-07-23
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.directors (director_id, director_lname, director_fname, birth_date, films_amount) FROM stdin;
1	Ritchie	Guy	1968-10-09	14
2	Hitchcock	Alfred	1899-08-13	36
3	Nolan	Christopher	1970-07-30	12
4	Cameron	James	1954-08-16	9
5	Kubrick	Stanley	1928-07-26	12
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: julia
--

COPY public.films (film_id, film_name, director_lname, director_fname, release_year, imdb) FROM stdin;
1	Wrath of Man	Ritchie	Guy	2021	7.1
2	Revolver	Ritchie	Guy	2005	6.3
3	Sherlock Holmes	Ritchie	Guy	2009	7.6
4	Inception	Nolan	Christopher	2010	8.8
5	The Prestige	Nolan	Chirstopher	2006	8.5
6	Seven Psychopaths	McDonagh	Martin	2012	7.1
\.


--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 5, true);


--
-- Name: directors_director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.directors_director_id_seq', 5, true);


--
-- Name: films_film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: julia
--

SELECT pg_catalog.setval('public.films_film_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

