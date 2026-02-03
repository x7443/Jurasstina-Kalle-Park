*** Settings ***
Documentation    Tests para Jurasstina-Kalle Park 
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***
Webbtestning av Jurasstina-Kalle Park
  Open Browser    http://127.0.0.1:8000/jurap.html      chrome
  Sleep    5s