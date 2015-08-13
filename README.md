Welcome to the world of Thermostats

= Data generation

    python ./ThermostatSimulator.py -n_thermostats 3 -n_ticks 50 -output_name output.csv

== Generate & send
Just redirect the generated output with netcat:

    python ./ThermostatSimulator.py -n_thermostats 3 -n_ticks 50 | nc localhost 7777

