from cohortextractor import StudyDefinition, patients, codelist_from_csv

asthma_dx_codes = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-ast.csv", system="snomed", column="code"
)
asthma_rx_codes = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-astrx.csv", system="snomed", column="code"
)


study = StudyDefinition(
    index_date="2021-01-20",  # Third Wednesday in January
    population=patients.satisfying("registered = 1 AND NOT has_died"),
    registered=patients.registered_as_of(
        "index_date",
        return_expectations={
            "incidence": 0.95,
            "date": {"earliest": "2000-01-01", "latest": "2099-12-31"},
        },
    ),
    has_died=patients.died_from_any_cause(
        on_or_before="index_date",
        return_expectations={
            "incidence": 0.95,
            "date": {"earliest": "2000-01-01", "latest": "2099-12-31"},
        },
    ),
    asthma_dx_today=patients.with_these_clinical_events(
        asthma_dx_codes,
        between=["index_date", "index_date"],
        return_expectations={
            "incidence": 0.05,
            "date": {"earliest": "2000-01-01", "latest": "2099-12-31"},
        },
    ),
    asthma_rx_today=patients.with_these_medications(
        asthma_rx_codes,
        between=["index_date", "index_date"],
        return_expectations={
            "incidence": 0.05,
            "date": {"earliest": "2000-01-01", "latest": "2099-12-31"},
        },
    ),
)
