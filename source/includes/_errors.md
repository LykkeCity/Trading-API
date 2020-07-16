# Error codes

Code | Meaning
---- | ---- 
`0` | Success 

## General network errors (10xx)

Code | Meaning | Description
---- | ---- | -----------
`1001` | RuntimeError | Internal Server Error

## Validation errors(11xx)

Code | Meaning | Description
---- | ---- | -----------
`1100` | ItemNotFound | resource not found (i.e. asset not found by provided ID)
`1101` | InvalidField | invalid field in the request (i.e. Price must be > 0)

## Logic errors(2xxx)

Code | Meaning 
---- | ---- 
`2000` | MeBadRequest
`2001` | MeLowBalance
`2202` | MeAlreadyProcessed
`2003` | MeDisabledAsset
`2004` | MeUnknownAsset
`2005` | MeNoLiquidity
`2006` | MeNotEnoughFunds
`2007` | MeDust
`2008` | MeReservedVolumeHigherThanBalance
`2009` | MeNotFound
`2010` | MeBalanceLowerThanReserved
`2011` | MeLeadToNegativeSpread
`2012` | MeTooSmallVolume
`2013` | MeInvalidFee
`2014` | MeInvalidPrice
`2015` | MeReplaced
`2016` | MeNotFoundPrevious
`2017` | MeDuplicate
`2018` | MeInvalidVolumeAccuracy
`2019` | MeInvalidPriceAccuracy
`2020` | MeInvalidVolume
`2021` | MeTooHighPriceDeviation
`2022` | MeInvalidOrderValue
`2023` | MeRuntime
