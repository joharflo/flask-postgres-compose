--
-- PostgreSQL database dump
--


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


--

CREATE DOMAIN public.year AS integer
	CONSTRAINT year_check CHECK (((VALUE >= 1901) AND (VALUE <= 2155)));


ALTER DOMAIN public.year OWNER TO shoro;


CREATE SEQUENCE public.items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_id_seq OWNER TO shoro;

--
-- Name: items; Type: TABLE; Schema: public; Owner: shoro
--

CREATE TABLE public.items (
    id integer DEFAULT nextval('public.items_id_seq'::regclass) NOT NULL,
    name text NOT NULL,
    description text NULL
);


ALTER TABLE public.items OWNER TO shoro;

--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: shoro
--

INSERT INTO public.items (name, description) VALUES ('SmartTV', 'Enjoy vibrant colors and sharp details');
INSERT INTO public.items (name, description) VALUES ('Refrigerator ', 'high-performance cooling unit designed to meet the demands of modern households and commercial environments');
INSERT INTO public.items (name, description) VALUES ('Mattress', 'Crafted from durable hardwood and upholstered with high-quality fabric');
