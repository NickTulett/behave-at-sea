Feature: Users can read the privacy policy

  Scenario Outline: Haxxor reads the privacy policy
    Given Haxxor goes to the Juice Shop
    When she opens the "<Hidden_Page>"
    # Then she sees she has solved the "Privacy Policy" challenge

    Examples:
      | Hidden_Page    |
      | Privacy Policy |
      | Score Board    |
