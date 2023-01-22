set terminal latex
set output './3911-gnuplottex-fig1.tex'
set title 'Plotf of cos(x)'
set ylabel 'cos(Θ) and sin(Θ)'
set ylabel 'Θ'
set yrange [-1:1]
set ytics 0,0.1,1
set ytics 0,1,pi
set xrange [-pi:pi]
unset key
plot cos(x)
