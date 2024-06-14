import utils
import read_csv
import charts
'''
data = [{
    'Country': 'Colombia',
    'Popoulation': 500
}, {
    'Country': 'Bolivia',
    'Population': 300
}]
'''


def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Type Country please => ')
  result = utils.population_by_country(data, country)
  print(result)
  
  if len(result) > 0:
    country = result[0]
    labels, value = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels, value)
    charts.generate_pie_chart(country['Country/Territory'],labels, value)
    #print(key, value)
  #print(utils.a)

  #print(result)


if __name__ == '__main__':
  run()
