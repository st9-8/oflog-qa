#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: st9_8

from settings import *
from IPython.display import display
from rdflib.namespace import FOAF, RDF, RDFS
from rdflib.tools.rdf2dot import rdf2dot
from rdflib import Graph, Literal, Namespace, URIRef
from utils import discretize_data, extract_action, sort_data, train_test_split, construct_sentences

import io
import logging
import pydotplus
import pandas as pd


# Load oflog ontology
oflog = Namespace(BASE_URI)


def extract_triples():
    """
        Function used to read and parse logs data
    """

    df = pd.read_csv(DATA_FILE)
    df = sort_data(df)
    train, test = train_test_split(df, test_size=0.4)

    frames = discretize_data(train)

    for key, value in frames.items():
        g = Graph()
        g.bind('oflog', oflog)
        g.bind('foaf', FOAF)

        logging.info(f'Processing triples for frame {key}...')

        for _, row in value.iterrows():
            student = URIRef(BASE_URI + row[SUBJECT])

            action, action_desc = extract_action(row[ACTION])
            action = URIRef(action)
            course = URIRef(BASE_URI + 'course-' + str(id(row[OBJECT])))
            info = URIRef(BASE_URI + 'info-' + str(id(row[INFORMATION])))

            g.add((student, RDF.type, oflog.LogUser))
            g.add((student, FOAF.name, Literal(row[SUBJECT])))
            g.add((student, oflog.makes, action))
            g.add((student, oflog.ip, Literal(row[IP])))
            g.add((action, RDF.type, oflog.LogAction))
            g.add((action, oflog.name, Literal(action_desc)))
            # g.add((action, oflog.at, Literal(row[date_field])))
            g.add((action, oflog.on, course))
            g.add((info, RDF.type, oflog.LogInformation))
            g.add((info, oflog.content, Literal(row[INFORMATION])))
            g.add((course, RDF.type, oflog.LogResourse))
            g.add((course, oflog.hasInfo, info))
            g.add((course, oflog.name, Literal(row[OBJECT])))

        logging.info(f'{len(g)} triples have been extracted from frame {key}.')

        draw_graph(g, key)
        construct_sentences(g, key)

    logging.info(f"All RDF graphs have been stored in '{GRAPH_FOLDER}'.")


def draw_graph(g, key):
    """
        Function used to draw RDF graph from triples and save it as image
    """
    stream = io.StringIO()
    rdf2dot(g, stream, opts={display})
    dot_graph = pydotplus.graph_from_dot_data(stream.getvalue())
    png_graph = dot_graph.create_jpg()

    if len(g):
        with open(GRAPH_FOLDER / f'frame_{key}.jpg', 'wb') as img:
            img.write(png_graph)
            logging.info(f'Frame {key} RDF graph drawed.')


if __name__ == '__main__':
    extract_triples()
