Feature: INEI work
  © 2009 by John Maling. All rights reserved.
  No part of this book may be reproduced in any written, electronic, recording, or photocopying form without written permission of the author, John Maling, photographer Grant Collier, or the publisher, Mile High Press, Ltd.
  Books may be purchased in quantity and/or special sales by contacting the publisher, Mile High Press, at PO Box 460880, Aurora CO 80046; 303-885-4460, by faxing 303-627-9184 or by email at MileHighPress@aol.com.

  Scenario: Search by zipcode
    Given:  I have 76228 in my address
    And:  The France as residence

    Scenario: Search by country number
      Given: The France as residence

    Scenario: Search by habitants number
      Given: The actual number of habitants is 250.000
