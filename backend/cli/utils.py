from app.db.base import SessionLocal

def get_db_session():
    return SessionLocal()

def format_table(headers, rows):
    """Simple table formatter for CLI output"""
    col_widths = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]
    
    def format_row(row):
        return " | ".join(str(item).ljust(width) for item, width in zip(row, col_widths))
    
    separator = "-+-".join("-" * width for width in col_widths)
    
    output = [format_row(headers), separator]
    output.extend(format_row(row) for row in rows)
    
    return "\n".join(output)
