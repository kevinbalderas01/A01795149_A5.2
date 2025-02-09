'''
sys -> To get parameters from terminal
os -> To manage files, creation and deletion
time -> To manage start and end time to measure execution
json -> To manage json files and getting content in the form of a dict
'''
# pylint: disable=invalid-name
import sys
import os
import time
import json


def read_json_file(filename):
    '''
    Función encargada de leer el archivo de tipo json
    '''

    with open(filename, 'r', encoding='utf-8') as jsonfile:
        result = json.loads(jsonfile.read())
    return result


def write_info_file(data):
    '''
    La función escriba la información en el archivo de salida correspondiente
    '''

    final_cost, final_time, start_time = data
    with open('SalesResults.txt', 'w', encoding='utf-8') as file:
        file.write(f'Final cost: {final_cost}\n')
        file.write(f'Tiempo de execucion en segundos: {final_time-start_time}')


def delete_final_file(path='SalesResults.txt'):
    '''
    Esta función elimina el archivo final en caso de existir
    para sobrescribirlo con cada ejecución
    '''
    if os.path.isfile(path):
        os.remove(path)


def get_cost_from_sale(sale, products):
    '''
    Esta función calcula el costo de cada item,
    Viendo el catalogo y multiplicando costo
    Por la cantidad de productos comprados
    '''
    cost = 0
    name = sale['Product']
    quantity = sale['Quantity']
    for product in products:
        if product['title'] == name:
            cost = product['price'] * quantity
    return cost


def calculate_cost(products, sales):
    '''
    Esta función calcula el costo de todos los productos de la venta,
    Por cada item vendido manda a llamar a otra función
    Para obtener el calulo de la venta basado en precio y cantidad.
    Al final devuelve la sumatoria global de cada item vendido
    '''
    total_cost = 0
    for sale in sales:
        cost_item = get_cost_from_sale(sale, products)
        total_cost += cost_item
    return round(total_cost, 2)


def main():
    '''
    Ejecución principal del programa
    '''
    start_time = time.time()
    delete_final_file()
    print('Inicio de programa')
    try:
        products_file, sales_file = sys.argv[1], sys.argv[2]
        result_products = read_json_file(products_file)
        results_sales = read_json_file(sales_file)
        final_cost = calculate_cost(result_products, results_sales)
        print(f'Final cost: {final_cost}')
        final_time = time.time()
        print(f'Tiempo de execucion en segundos: {final_time-start_time}')
        write_info_file((final_cost, final_time, start_time))
        print('Fin de execución')
    except (FileNotFoundError, IndexError) as error:
        print('No file was found', error)


if __name__ == '__main__':
    main()
