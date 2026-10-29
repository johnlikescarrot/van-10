#let note(title, body) = block(fill: rgb("#eef6f6"), stroke: (left: 3pt + rgb("#36938d")), inset: 10pt, radius: 3pt, width: 100%, breakable: true)[#strong[#title] #linebreak() #body]
#let passage(title, body) = block(fill: rgb("#f8f6ee"), stroke: 0.5pt + rgb("#d8d2bf"), inset: 11pt, radius: 3pt, width: 100%, breakable: true)[#strong[#title] #linebreak() #body]
#let q(n, body) = block(above: 3pt, below: 3pt, inset: (bottom: 4pt), breakable: false)[#strong[Câu #n.] #body]
#let opts(a,b,c,d) = [A. #a #linebreak() B. #b #linebreak() C. #c #linebreak() D. #d]
