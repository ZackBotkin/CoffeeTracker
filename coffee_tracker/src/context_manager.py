from coffee_tracker.src.io.query_runner import QueryRunner


class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()


    def record_coffee(self, description, oz):
        self.query_runner.insert_coffee(description, oz)

    def get_coffees(self):
        coffees = self.query_runner.get_coffees()
        return coffees
