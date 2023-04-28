*** Settings ***
Library  file.py
Library    OperatingSystem

*** Variables ***
${input}   52
${input2}    25
${expected}   77
*** Keywords ***
keyword1
    [Arguments]   ${val}  ${val2}
    ${result}    file.addition   ${val}  ${val2}
    Should Be Equal As Integers    ${result}     ${expected}

*** Test Cases ***
Testcase
    [Documentation]
    []
    keyword1    ${input}    ${input2}
    Log File  file://output.txt



Scenario : Log In function
Given : URL is up and runnning

When  User enter usermae
And  Use ri
And User
Then
And
