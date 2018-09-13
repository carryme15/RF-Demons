*** Settings ***
Library  CaculatorLibrary.py
Test Template  ${expression} should be equal ${expected}

*** Keywords ***
${expression} should be equal ${expected}
    ${result} =  caculate  C${expression}=
    should be equal  ${result}  ${expected}

*** Test Cases ***
kinds of valid expression
    1 + 1  2
    1 - 9  -8
