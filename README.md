# VC-tax-calc

Fun little challenge as part of a job application

This is a command line program that replicates the functionality of the [ATO Simple Tax Calculator](https://www.ato.gov.au/Calculators-and-tools/Host/?anchor=STC&anchor=STC#STC/questions)


## Setup & Run Instructions
### Docker
```shell
git clone https://github.com/Gimb0/VC-tax-calc.git
cd VC-tax-calc
docker build -t vc-tax-calc .
docker run -it vc-tax-calc
```

### Python
```shell
git clone https://github.com/Gimb0/VC-tax-calc.git
cd VC-tax-calc
pip3 install -r requirements.txt
python3 src/main.py
```


To add more Financial Year data run
```shell
python3 src/taxRatesHandler.py -i
```
This will provide you with a cmd line user interface where you can input the necessary data
