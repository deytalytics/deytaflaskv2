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
-- Name: deypay_user; Type: TABLE; Schema: public; Owner: kbmymanebzaprn
--


CREATE TABLE public.deypay_user (
    id integer NOT NULL,
    username character varying(15),
    email character varying(50),
    password character varying(80),
    created_ts timestamp without time zone,
    updated_ts timestamp without time zone
);


ALTER TABLE public.deypay_user OWNER TO kbmymanebzaprn;

--
-- Name: deypay_user_id_seq; Type: SEQUENCE; Schema: public; Owner: kbmymanebzaprn
--

CREATE SEQUENCE public.deypay_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.deypay_user_id_seq OWNER TO kbmymanebzaprn;

--
-- Name: deypay_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kbmymanebzaprn
--

ALTER SEQUENCE public.deypay_user_id_seq OWNED BY public.deypay_user.id;


--
-- Name: deypay_user id; Type: DEFAULT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.deypay_user ALTER COLUMN id SET DEFAULT nextval('public.deypay_user_id_seq'::regclass);


--
-- Data for Name: deypay_user; Type: TABLE DATA; Schema: public; Owner: kbmymanebzaprn
--

COPY public.deypay_user (id, username, email, password, created_ts, updated_ts) FROM stdin;
4	jdey	James.m.dey@gmail.com	sha256$cldGdBNb$ca51fe58ad0a235d885a8297331f806dd89cbab9baa6d7c6285f3f218cf39d15	2019-01-12 10:56:21.365038	2019-01-12 10:56:21.365038
5	jdey123	james_dey@hotmail.com	sha256$yhpPoeF7$aa297c9a921656f2a4c194c23107f2b222fdaf0d4d98ff867ee50ea5f6d8c5c8	2019-01-12 11:08:58.939911	2019-01-12 11:08:58.939911
6	james123	james.dey@deytalytics.com	sha256$djJjirpR$86d576fd01bba7f25313700e88d6803663a62ffa39f6ee8d641a0e675d02d7bd	2019-01-27 20:36:33.85397	2019-01-27 20:36:33.85397
9	Deytalytics	james.m.dey@gmail.com	sha256$2yYp25On$3d3e0f34e1d75fbe3216d727c9394ca9470cb59920ce64158c491e5c50bd3c52	2019-01-27 20:41:14.865117	2019-01-27 20:41:14.865117
10	Charlie	charliedey@hotmail.com	sha256$syeEdplv$1411aea25408008fcb1ebf31199e55367a8b7c86ab19028bf673a4f40a35bbd7	2019-01-27 20:52:46.461387	2019-01-27 20:52:46.461387
\.


--
-- Name: deypay_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kbmymanebzaprn
--

SELECT pg_catalog.setval('public.deypay_user_id_seq', 10, true);


--
-- Name: deypay_user deypay_user_email_key; Type: CONSTRAINT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.deypay_user
    ADD CONSTRAINT deypay_user_email_key UNIQUE (email);


--
-- Name: deypay_user deypay_user_pkey; Type: CONSTRAINT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.deypay_user
    ADD CONSTRAINT deypay_user_pkey PRIMARY KEY (id);


--
-- Name: deypay_user deypay_user_username_key; Type: CONSTRAINT; Schema: public; Owner: kbmymanebzaprn
--

ALTER TABLE ONLY public.deypay_user
    ADD CONSTRAINT deypay_user_username_key UNIQUE (username);


--
-- PostgreSQL database dump complete
--

