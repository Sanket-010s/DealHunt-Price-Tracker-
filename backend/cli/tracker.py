#!/usr/bin/env python3
import sys
import argparse
from cli.commands import (
    add_product,
    list_products,
    remove_product,
    check_product,
    show_history,
    run_server
)

def main():
    parser = argparse.ArgumentParser(description="Price Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a product to track")
    add_parser.add_argument("url", help="Product URL")
    add_parser.add_argument("--name", help="Product name (optional, will be scraped)")
    add_parser.add_argument("--currency", default="USD", help="Currency code")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List all products")
    list_parser.add_argument("--active-only", action="store_true", help="Show only active products")
    
    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a product")
    remove_parser.add_argument("id", type=int, help="Product ID")
    
    # Check command
    check_parser = subparsers.add_parser("check", help="Check product prices")
    check_parser.add_argument("--id", type=int, help="Product ID (optional, checks all if not provided)")
    
    # History command
    history_parser = subparsers.add_parser("history", help="Show price history")
    history_parser.add_argument("id", type=int, help="Product ID")
    history_parser.add_argument("--days", type=int, default=30, help="Number of days to show")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run the API server")
    run_parser.add_argument("--host", help="Host address")
    run_parser.add_argument("--port", type=int, help="Port number")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute command
    if args.command == "add":
        add_product(args.url, args.name, args.currency)
    elif args.command == "list":
        list_products(args.active_only)
    elif args.command == "remove":
        remove_product(args.id)
    elif args.command == "check":
        check_product(args.id)
    elif args.command == "history":
        show_history(args.id, args.days)
    elif args.command == "run":
        run_server(args.host, args.port)

if __name__ == "__main__":
    main()
