from yaml import full_load


class ImportPricing:

    def __init__ (self, filename):
        with open(filename) as file:
            self.contents = full_load(file)

    def get_data(self, key1, key2, element):
        return self.contents[key1][key2][element]
    
    def hardware_costs(self, containertype, cpu, ram, storage, backup):
        cpucost = self.get_data('platform', containertype, 'cpu')
        ramcost = self.get_data('platform', containertype, 'ram')
        storagecost = self.get_data('platform', containertype, 'storage')
        backupcost = self.get_data('platform', containertype, 'backup')
        if backup == "Yes":
            return (cpucost * cpu) + (ramcost * ram) + ((storagecost+backupcost) * storage)
        elif backup == "No":
            return (cpucost * cpu) + (ramcost * ram) + (storagecost * storage)
    
    def support_costs(self, cost, number):
        dayrate = self.get_data("division", "PLTE", "dayrate")
        containercharge = self.get_data("division", "PLTE", "containercharge")
        contingency = self.get_data("division", "PLTE", "contingency")
        return((cost + dayrate) + (number * containercharge) * contingency)
    
    
        