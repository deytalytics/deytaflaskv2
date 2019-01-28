--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-1.pgdg16.04+1)
-- Dumped by pg_dump version 10.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: kbmymanebzaprn
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    date_created timestamp without time zone,
    date_modified timestamp without time zone,
    name character varying(128) NOT NULL,
    email character varying(128) NOT NULL,
    password character varying(192) NOT NULL,
    role smallint NOT NULL,
    status smallint NOT NULL
);


ALTER TABLE public.auth_user OWNER TO kbmymanebzaprn;

--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: kbmymanebzaprn
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO kbmymanebzaprn;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kbmymanebzaprn
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: kbmymanebzaprn
--

COPY public.auth_user (id, date_created, date_modified, name, email, password, role, status) FROM stdin;
\.


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kbmymanebzaprn
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user auth_user_email_key; Type: CONSTRAINT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_email_key UNIQUE (email);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

