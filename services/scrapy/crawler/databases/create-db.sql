--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

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
-- Name: voz_link; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_link (
    id integer NOT NULL,
    link character varying,
    spider_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.voz_link OWNER TO postgres;

--
-- Name: voz_link_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voz_link_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voz_link_id_seq OWNER TO postgres;

--
-- Name: voz_link_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voz_link_id_seq OWNED BY public.voz_link.id;


--
-- Name: voz_rawcomment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_rawcomment (
    id character varying NOT NULL,
    "time" timestamp without time zone NOT NULL,
    author character varying,
    topic character varying,
    content character varying,
    spider_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.voz_rawcomment OWNER TO postgres;

--
-- Name: voz_spider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_spider (
    id integer NOT NULL,
    status character varying,
    reason character varying,
    time_start timestamp without time zone,
    time_end timestamp without time zone,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.voz_spider OWNER TO postgres;

--
-- Name: voz_spider_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voz_spider_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voz_spider_id_seq OWNER TO postgres;

--
-- Name: voz_spider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voz_spider_id_seq OWNED BY public.voz_spider.id;


--
-- Name: voz_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_stats (
    id integer NOT NULL,
    num_stock integer,
    num_rawcomment integer,
    num_link integer,
    stats jsonb,
    spider_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.voz_stats OWNER TO postgres;

--
-- Name: voz_stats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voz_stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voz_stats_id_seq OWNER TO postgres;

--
-- Name: voz_stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voz_stats_id_seq OWNED BY public.voz_stats.id;


--
-- Name: voz_stock_stats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_stock_stats (
    id integer NOT NULL,
    stock character varying NOT NULL,
    num integer NOT NULL,
    spider_id integer NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.voz_stock_stats OWNER TO postgres;

--
-- Name: voz_stock_stats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voz_stock_stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voz_stock_stats_id_seq OWNER TO postgres;

--
-- Name: voz_stock_stats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voz_stock_stats_id_seq OWNED BY public.voz_stock_stats.id;


--
-- Name: voz_stockmapping; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voz_stockmapping (
    id integer NOT NULL,
    stock character varying,
    spider_id integer NOT NULL,
    voz_commentid character varying NOT NULL,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    "time" timestamp without time zone
);


ALTER TABLE public.voz_stockmapping OWNER TO postgres;

--
-- Name: voz_stockmapping_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voz_stockmapping_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voz_stockmapping_id_seq OWNER TO postgres;

--
-- Name: voz_stockmapping_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voz_stockmapping_id_seq OWNED BY public.voz_stockmapping.id;


--
-- Name: voz_link id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_link ALTER COLUMN id SET DEFAULT nextval('public.voz_link_id_seq'::regclass);


--
-- Name: voz_spider id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_spider ALTER COLUMN id SET DEFAULT nextval('public.voz_spider_id_seq'::regclass);


--
-- Name: voz_stats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stats ALTER COLUMN id SET DEFAULT nextval('public.voz_stats_id_seq'::regclass);


--
-- Name: voz_stock_stats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stock_stats ALTER COLUMN id SET DEFAULT nextval('public.voz_stock_stats_id_seq'::regclass);


--
-- Name: voz_stockmapping id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stockmapping ALTER COLUMN id SET DEFAULT nextval('public.voz_stockmapping_id_seq'::regclass);


--
-- Data for Name: voz_link; Type: TABLE DATA; Schema: public; Owner: postgres
--


--
-- Name: voz_link_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voz_link_id_seq', 5577, true);


--
-- Name: voz_spider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voz_spider_id_seq', 24, true);


--
-- Name: voz_stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voz_stats_id_seq', 177, true);


--
-- Name: voz_stock_stats_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voz_stock_stats_id_seq', 1670, true);


--
-- Name: voz_stockmapping_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voz_stockmapping_id_seq', 31315, true);


--
-- Name: voz_link voz_link_link_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_link
    ADD CONSTRAINT voz_link_link_key UNIQUE (link);


--
-- Name: voz_link voz_link_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_link
    ADD CONSTRAINT voz_link_pkey PRIMARY KEY (id);


--
-- Name: voz_rawcomment voz_rawcomment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_rawcomment
    ADD CONSTRAINT voz_rawcomment_pkey PRIMARY KEY (id);


--
-- Name: voz_spider voz_spider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_spider
    ADD CONSTRAINT voz_spider_pkey PRIMARY KEY (id);


--
-- Name: voz_stats voz_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stats
    ADD CONSTRAINT voz_stats_pkey PRIMARY KEY (id);


--
-- Name: voz_stock_stats voz_stock_stats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stock_stats
    ADD CONSTRAINT voz_stock_stats_pkey PRIMARY KEY (id);


--
-- Name: voz_stock_stats voz_stock_stats_stock_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stock_stats
    ADD CONSTRAINT voz_stock_stats_stock_key UNIQUE (stock);


--
-- Name: voz_stockmapping voz_stockmapping_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stockmapping
    ADD CONSTRAINT voz_stockmapping_pkey PRIMARY KEY (id);


--
-- Name: voz_stockmapping voz_stockmapping_voz_commentid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stockmapping
    ADD CONSTRAINT voz_stockmapping_voz_commentid_key UNIQUE (voz_commentid);


--
-- Name: voz_link voz_link_spider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_link
    ADD CONSTRAINT voz_link_spider_id_fkey FOREIGN KEY (spider_id) REFERENCES public.voz_spider(id) ON DELETE CASCADE;


--
-- Name: voz_rawcomment voz_rawcomment_spider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_rawcomment
    ADD CONSTRAINT voz_rawcomment_spider_id_fkey FOREIGN KEY (spider_id) REFERENCES public.voz_spider(id) ON DELETE CASCADE;


--
-- Name: voz_stats voz_stats_spider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stats
    ADD CONSTRAINT voz_stats_spider_id_fkey FOREIGN KEY (spider_id) REFERENCES public.voz_spider(id) ON DELETE CASCADE;


--
-- Name: voz_stock_stats voz_stock_stats_spider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stock_stats
    ADD CONSTRAINT voz_stock_stats_spider_id_fkey FOREIGN KEY (spider_id) REFERENCES public.voz_spider(id) ON DELETE CASCADE;


--
-- Name: voz_stockmapping voz_stockmapping_spider_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stockmapping
    ADD CONSTRAINT voz_stockmapping_spider_id_fkey FOREIGN KEY (spider_id) REFERENCES public.voz_spider(id) ON DELETE CASCADE;


--
-- Name: voz_stockmapping voz_stockmapping_voz_commentid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voz_stockmapping
    ADD CONSTRAINT voz_stockmapping_voz_commentid_fkey FOREIGN KEY (voz_commentid) REFERENCES public.voz_rawcomment(id) ON DELETE CASCADE;

