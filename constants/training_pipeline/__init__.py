# The target column that we have to predict
TARGET_COLUMN = "churn"

# Columns that are in use and needed to be dropped
COLS_TO_DROP = [' "recordID"',
                'state',
                'customer_id',
                'total_day_charge',
                'total_eve_charge',
                'total_night_charge',
                'total_intl_charge']