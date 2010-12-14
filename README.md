Mysql bin look
==============

Read and seek mysqlbinlog file.

Install
-------

		python setup.py build
		sudo python setup.py install

Use
---

_mysqlbinlook_ read sql from stdin and seek a pattern

		mysqlbinlog mysql-bin.* | mysqlbinlook date_format_types

