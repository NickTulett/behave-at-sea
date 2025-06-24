Feature: Users can find hidden pages

  Scenario Outline: Haxxor finds hidden pages
    Given Haxxor goes to the Juice Shop
    When she opens the "<Hidden Page>"
    Then she sees she has solved the "<Hidden Page>" challenge

    Examples:
      | Hidden Page    |
      | Privacy Policy |
      | Score Board    |
