--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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
-- Name: chat_history_companion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chat_history_companion (
    session_id character(50) NOT NULL,
    created_at date NOT NULL,
    chat jsonb
);


ALTER TABLE public.chat_history_companion OWNER TO postgres;

--
-- Data for Name: chat_history_companion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.chat_history_companion (session_id, created_at, chat) FROM stdin;
399dce28-29a2-4b9e-8431-db2fc2f10797              	2023-04-11	{"messages": [{"sender": "user", "content": "Pregunta 1", "timestamp": "2023-04-11T12:35:10Z"}, {"sender": "assistant", "content": "Respuesta 1", "timestamp": "2023-04-11T12:35:15Z"}, {"sender": "user", "content": "Pregunta 2", "timestamp": "2023-04-11T12:36:22Z"}, {"sender": "assistant", "content": "Respuesta 2", "timestamp": "2023-04-11T12:36:30Z"}]}
2f0c45f6-cb69-4acd-bc2b-ccf22f195164              	2023-04-11	{"messages": [{"sender": "user", "content": "Hello chat!", "timestamp": "2023-04-11T12:35:10Z"}, {"sender": "assistant", "content": "How is going your day?", "timestamp": "2023-04-11T12:35:15Z"}, {"sender": "user", "content": "Excelent, I rellay need a Google Drive tutorial to create, update and share a csv", "timestamp": "2023-04-11T12:36:22Z"}, {"sender": "assistant", "content": "Sure, let me help you with that....", "timestamp": "2023-04-11T12:36:30Z"}]}
\.


--
-- Name: chat_history_companion chat_history_companion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chat_history_companion
    ADD CONSTRAINT chat_history_companion_pkey PRIMARY KEY (session_id, created_at);


--
-- Name: idx_chat_history_companion_created_at; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_chat_history_companion_created_at ON public.chat_history_companion USING btree (created_at);


--
-- Name: idx_chat_history_companion_session_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_chat_history_companion_session_id ON public.chat_history_companion USING btree (session_id);


--
-- PostgreSQL database dump complete
--

