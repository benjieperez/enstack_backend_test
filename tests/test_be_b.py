from ..test_b import transform_data 

# Test cases
SECTION_A = [
    {"manager_name": "nssi", "login_name": "nishanthi"},
    {"manager_name": "mbarcelona", "login_name ": "nssi"},
    {"manager_name": "nishanthi", "login_name": "markcorderoi"},
    {"manager_name": "mbarcelona", "login_name ": "richard"},
    {"manager_name": "letecia", "login_name ": "rudy"}
]

EXPECTED_SECTION_B = [
    {
        "name": "letecia",
        "subordinate": [
            {
                "name": "rudy"
            }
        ]
    },
    {
        "name": "mbarcelona",
        "subordinate": [
            {
                "name": "nssi",
                "subordinate": [
                    {
                        "name": "nishanthi",
                        "subordinate": [
                            {
                                "name": "markcorderoi"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "richard"
            }
        ]
    }
]

# Test for Section B transforming from Section A
def test_json_rewrite():
    result = transform_data(SECTION_A)
    assert result == EXPECTED_SECTION_B