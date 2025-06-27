# PHP - PHP Unit

This kata help you practice test doubles and PHPUnit

For full instructions about the problem see [home readme](../README.md)

__//!\\ PHP 8.1 is necessary for this kata to work__

## Installing

You need a working PHP version, and [composer](https://getcomposer.org/) installed

Just run:
> composer install

## Running the tests
Your IDE should be able to launch the tests easily, but if you want to launch from command line:
> ./vendor/bin/phpunit tests

## Getting coverage
You will need XDebug installed an configured, see [here](https://www.lambdatest.com/blog/phpunit-code-coverage-report-html/) for more info (article for Windows)

The configuration you should put in your php.ini once you have installed XDebug is:
```
[XDebug]
zend_extension=xdebug
xdebug.mode=coverage
xdebug.start_with_request=trigger
```

Then to launch coverage: 

> ./vendor/bin/phpunit --coverage-html coverage --coverage-filter src tests
