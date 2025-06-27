<?php

use kata\CurrencyConverter;
use kata\external\ConversionRateApi;
use kata\external\CurrencyIsoCode;
use kata\model\Currency;
use kata\model\Money;
use PHPUnit\Framework\TestCase;

// Fake : retourne un taux fixe pour chaque paire
class FakeConversionRateApi extends ConversionRateApi {
    public function getRate(CurrencyIsoCode $source, CurrencyIsoCode $target): float {
        if ($source === CurrencyIsoCode::USD && $target === CurrencyIsoCode::EUR) return 0.9;
        if ($source === CurrencyIsoCode::EUR && $target === CurrencyIsoCode::USD) return 1.1;
        if ($source === $target) return 1.0;
        return 2.0; // valeur par défaut pour les autres cas
    }
}

// Stub : retourne toujours 1.0
class StubConversionRateApi extends ConversionRateApi {
    public function getRate(CurrencyIsoCode $source, CurrencyIsoCode $target): float {
        return 1.0;
    }
}

class CurrencyConverterTest extends TestCase
{
    public function testSumWithFakeApi() : void {
        $api = new FakeConversionRateApi();
        $converter = new CurrencyConverter($api);
        $result = $converter->sum(Currency::Euro, [
            new Money(100, Currency::Euro),
            new Money(100, Currency::Dollar)
        ]);
        // 100 EUR + (100 USD * 0.9) = 100 + 90 = 190 EUR
        $this->assertEquals(190, $result->amount);
        $this->assertEquals(Currency::Euro, $result->currency);
    }

    public function testSumWithStubApi() : void {
        $api = new StubConversionRateApi();
        $converter = new CurrencyConverter($api);
        $result = $converter->sum(Currency::Dollar, [
            new Money(50, Currency::Dollar),
            new Money(50, Currency::Euro)
        ]);
        // 50 USD + (50 EUR * 1.0) = 50 + 50 = 100 USD
        $this->assertEquals(100, $result->amount);
        $this->assertEquals(Currency::Dollar, $result->currency);
    }

    public function testSumWithSameCurrency() : void {
        // Ce test n'appelle pas l'API, mais c'est bien de le garder pour la logique interne.
        $api = $this->createMock(ConversionRateApi::class);
        $api->expects($this->never())->method('getRate'); // Mock pour vérifier que getRate n'est jamais appelée
        
        $converter = new CurrencyConverter($api);
        $result = $converter->sum(Currency::Yen, [
            new Money(10, Currency::Yen),
            new Money(20, Currency::Yen)
        ]);
        $this->assertEquals(30, $result->amount);
        $this->assertEquals(Currency::Yen, $result->currency);
    }

    public function testSumWithApiThrowingException() : void {
        // Mock : Simule une erreur de l'API
        $api = $this->createMock(ConversionRateApi::class);
        $api->method('getRate')->will($this->throwException(new \Exception("API error")));

        $converter = new CurrencyConverter($api);
        $this->expectException(\Exception::class);
        $converter->sum(Currency::Euro, [new Money(1, Currency::Pound)]);
    }
} 