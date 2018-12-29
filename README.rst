Purpose
=======

"blacktop" is a wrapper around the code formatter "black":
https://github.com/ambv/black

It monkeypatches black to prefer single-quoted strings and then reinvokes black.

This is meant as a temporary tool while waiting to see if the Python community
can decide on a preferred quoting style.  If black gains enough momentum, it may
well sway the community to prefer double quotes, though there are other tools
(such as Orange is the new black, Oitnb, https://pypi.org/project/oitnb/) which
are biased toward single quotes.

Reformatting code is easy; making changes to existing coding standards is hard.
Without a compelling reason, these standards are unlikely to change.  Until
either the Python community achieve a dominant quoting style, or popular Python
tooling converges on a preferred style, coding standards that dictate the
use of single quotes will prevent the use of black as-is.
