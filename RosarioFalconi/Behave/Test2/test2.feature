Feature: This a sample feature with background
Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500,
cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen.
No sólo sobrevivió 500 años

Background: This is a background
  Given I login application
  When I click on my User icon
  Then I see My Profile

  Scenario: Change user password

    Given I select change password
    When  I save my new password
    Then I should see confirmation message

  Scenario: Change user picture

    Given I select change picture
    When I select a new image from my pc
    Then I see new picture loaded