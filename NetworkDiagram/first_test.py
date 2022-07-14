import pyyed

g = pyyed.Graph()

g.add_node('foo', font_family="Zapfino")
g.add_node('foo2', shape="roundrectangle", font_style="bolditalic", underlined_text="true")

g.add_edge('foo1', 'foo2')
g.add_node('abc', font_size="72", height="100", shape_fill="#FFFFFF")

g.add_node('bar', label="Multi\nline\ntext")
g.add_node('foobar', label="""Multi
    Line
    Text!""")

g.add_edge('foo', 'foo1', label="EDGE!", width="3.0", color="#0000FF",
               arrowhead="white_diamond", arrowfoot="standard", line_type="dotted")

print(g.get_graph())

# To write to file:
with open('test_graph.graphml', 'w') as fp:
    fp.write(g.get_graph())

# Or:
g.write_graph('example.graphml')

# Or, to pretty-print with whitespace:
g.write_graph('pretty_example.graphml', pretty_print=True)