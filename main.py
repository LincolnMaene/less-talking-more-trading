from datetime import datetime
import quote_generator
import instruments_data_generator
import option_chains_generator
import datetime
def main():

    start_date=datetime.datetime.strptime('04-23-2020', '%m-%d-%Y')
    end_date=datetime.datetime.strptime('05-01-2024', '%m-%d-%Y')


    option_chains_generator.generate_options_calls_date('AAPL', 300, start_date, end_date)








if __name__ == "__main__":
    main()
