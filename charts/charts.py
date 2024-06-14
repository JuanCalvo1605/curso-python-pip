import matplotlib.pyplot as pylot

def generaCharts():
    labels = ['A','B', 'C']
    values = [200,34,120]
    
    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig('pie.png')
    pylot.close()