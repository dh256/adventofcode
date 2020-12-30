from Tickets import Tickets

tickets = Tickets('input.txt')
error_rate = tickets.scanning_error_rate()
print(f'Part 1: {error_rate}')

deperature_fields = tickets.departure_fields()
print(f'Part 2: {deperature_fields}')

