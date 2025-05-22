import mock
import builtins
import main

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q1(capfd, monkeypatch):
    input_output = {
        '4, 2016': '2020 2024 2028 2032 ',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q1()
        out, _ = capfd.readouterr()
        assert out == v

def test_q2(capfd, monkeypatch):
    input_output = {
        '-1, 6, 4, 5': 'Primo\nNão\nNão\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q2()
        out, _ = capfd.readouterr()
        assert out == v

def test_q3(capfd, monkeypatch):
    input_output = {
        '-4, 3.2, 5, 2.5': '10.70\n3.57\n',
        '-1': '0.00\n0.00\n',
        '0,-1,-2,-3': '0.00\n0.00\n',
        '-1,10,10': '20.00\n10.00\n',        
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q3()
        out, _ = capfd.readouterr()
        assert out == v

def test_q4(capfd, monkeypatch):
    input_output = {
        '80,1': '90.00\n',
        '200,3': '1470.00\n',
        '200,10': '2100.00\n',
        '2100,0': 'Valor inválido\n',
        '0,1': '90.00\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q4()
        out, _ = capfd.readouterr()
        assert out == v

def test_q5(capfd, monkeypatch):
    input_output = {
        '34.0,F': '1.11 C\n274.26 K\n',
        '-8.0,K': 'Valor de temperatura abaixo do minimo\n',
        '29.0,K': '-244.15 C\n-407.47 F\n',
        '-237.0,C': '-394.60 F\n36.15 K\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q5()
        out, _ = capfd.readouterr()
        assert out == v

 