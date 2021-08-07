import pydot
import nlp_41


sentences = nlp_41.get_chunked_sentences()
edges = []
for chunks in sentences:
    for index, chunk in enumerate(chunks):
        if int(chunk.dst) != -1:
            source = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
            target = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunks[int(chunk.dst)].morphs])
            edges.append([source, target])

pydot_node = pydot.Node('node')
graph = pydot.graph_from_edges(edges)
graph.add_node(pydot_node)
graph.write_png('./nlp_44.png')
