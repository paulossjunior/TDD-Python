
from behave import *
from src.BDD.application.calculator import Calculator

@given(u'I am using the calculator')
def step_impl(context):
    context.calculadora = Calculator()

@given(u'I input 2 add 2')
def step_impl(context):
    context.actual_result = context.calculadora.add(2 , 2)

@then(u'I should see 4')
def step_impl(context):
    expected_result = 4
    assert(expected_result == context.actual_result)

@given(u'I input {value_one:d} add {value_two:d}')
def step_impl(context,value_one, value_two):
    context.actual_result = context.calculadora.add(value_one , value_two)

@then(u'I should see {expected_result:d}')
def step_impl(context, expected_result ):
    assert(expected_result == context.actual_result)
