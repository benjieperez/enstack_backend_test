from ..test_a import shuffle_tuples

# Test data
EXPECTED_TUPLES = [(x, y) for y in range(4) for x in range(14)]

def test_shuffle_verification():
    """Test that shuffle maintains all elements (like the example verification)."""
    
    # Shuffle the list
    shuffled_tuples = shuffle_tuples(EXPECTED_TUPLES)
    
    # Verify all elements are present
    assert set(EXPECTED_TUPLES) == set(shuffled_tuples), "Shuffled list is missing elements"
    assert len(EXPECTED_TUPLES) == len(shuffled_tuples), "Shuffled list has different length"

def test_shuffle_changes_order():
    """Test that shuffle actually changes the order."""
    shuffled_tuples = shuffle_tuples(EXPECTED_TUPLES)
    
    # Verify the order changed
    assert shuffled_tuples != EXPECTED_TUPLES

def test_shuffle_preserves_elements():
    """Test that all individual elements are preserved."""
    shuffled_tuples = shuffle_tuples(EXPECTED_TUPLES)
    
    # Count occurrences of each tuple
    from collections import Counter
    assert Counter(EXPECTED_TUPLES) == Counter(shuffled_tuples)

def test_shuffle_doesnt_modify_original():
    """Test that original list remains unchanged."""
    original_copy = EXPECTED_TUPLES.copy()
    _ = shuffle_tuples(EXPECTED_TUPLES)
    
    assert EXPECTED_TUPLES == original_copy