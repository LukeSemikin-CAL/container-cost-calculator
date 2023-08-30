from modules.import_prices.pricing import ImportPricing

class CostCalculator:

    def __init__(self):
        self.pricing = ImportPricing("modules/import_prices/costs.yaml")

    def get_prices(self):
        return [
            {
                'name': 'HX',
                'cpu': "%0.2f" % self.pricing.get_data("platform", "Hyperflex", "cpu"),
                'ram':  "%0.2f" % self.pricing.get_data("platform", "Hyperflex", "ram"),
                'storage': "%0.2f" % self.pricing.get_data("platform", "Hyperflex", "storage"),
                'backup': "%0.2f" % self.pricing.get_data("platform", "Hyperflex", "backup"),
            },
            {
                'name': 'Blades',
                'cpu': "%0.2f" % self.pricing.get_data("platform", "Blades", "cpu"),
                'ram':  "%0.2f" % self.pricing.get_data("platform", "Blades", "ram"),
                'storage': "%0.2f" % self.pricing.get_data("platform", "Blades", "storage"),
                'backup': "%0.2f" % self.pricing.get_data("platform", "Blades", "backup"),
            }
        ]
    
    def get_outputs(self,containertype, cpu, ram, storage, backup, containernumber):
        hardwarecosts = self.pricing.hardware_costs(containertype, cpu, ram, storage, backup)
        supportcosts = self.pricing.support_costs(hardwarecosts, containernumber)
        return [
            {
                'infracost': "%0.2f" % hardwarecosts,
                'infratotalcost': "%0.2f" % (hardwarecosts * containernumber),
                'pltecost': "%0.2f" % supportcosts
            }
        ]