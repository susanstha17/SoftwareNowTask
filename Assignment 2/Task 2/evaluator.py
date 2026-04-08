import os

# Converts a mathematical expression string into a list of tokens
# Tokens can be numbers, operators (+, -, *, /), parentheses, or END
def tokenize(expr):
    tokens = []
    i = 0

    while i < len(expr):
        c = expr[i]

        if c.isspace():  # skip whitespace
            i += 1
            continue

        # number token (supports decimals)
        if c.isdigit() or c == '.':
            start = i
            dot_count = 0

            # handle numbers with a single decimal point
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                if expr[i] == '.':
                    dot_count += 1
                    if dot_count > 1:
                        raise ValueError("Invalid number")
                i += 1

            tokens.append(("NUM", expr[start:i]))
            continue

        # operator token
        if c in "+-*/":
            tokens.append(("OP", c))
            i += 1
            continue

        # left parenthesis
        if c == "(":
            tokens.append(("LPAREN", "("))
            i += 1
            continue

        # right parenthesis
        if c == ")":
            tokens.append(("RPAREN", ")"))
            i += 1
            continue

        # invalid character
        raise ValueError("Invalid character")

    tokens.append(("END", ""))  # mark the end of the expression
    return tokens


# Format tokens into a string representation for debugging/output
def format_tokens(tokens):
    parts = []
    for t, v in tokens:
        if t == "END":
            parts.append("[END]")
        else:
            parts.append(f"[{t}:{v}]")
    return " ".join(parts)


# PARSER
# Recursive descent parser for expressions

# Handles addition and subtraction
def parse_expression(tokens, pos):
    node, value, pos = parse_term(tokens, pos)  # parse first term

    # parse subsequent + or - terms
    while pos < len(tokens) and tokens[pos][0] == "OP" and tokens[pos][1] in "+-":
        op = tokens[pos][1]
        pos += 1
        right_node, right_val, pos = parse_term(tokens, pos)

        if op == "+":
            value += right_val
        else:
            value -= right_val

        # build the expression tree string
        node = f"({op} {node} {right_node})"

    return node, value, pos


# Handles multiplication, division, and implicit multiplication
def parse_term(tokens, pos):
    node, value, pos = parse_factor(tokens, pos)

    while True:
        # explicit * or /
        if pos < len(tokens) and tokens[pos][0] == "OP" and tokens[pos][1] in "*/":
            op = tokens[pos][1]
            pos += 1
        # implicit multiplication (e.g., 2(3+4))
        elif pos < len(tokens) and tokens[pos][0] in ("NUM", "LPAREN"):
            op = "*"
        else:
            break

        right_node, right_val, pos = parse_factor(tokens, pos)

        # compute value (handle division by zero safely)
        if op == "*":
            value *= right_val
        else:
            if right_val == 0:
                value = float("inf")  # mark division by zero
            else:
                value /= right_val

        # build tree representation
        node = f"({op} {node} {right_node})"

    return node, value, pos


# Handles numbers, unary negation, and parentheses
def parse_factor(tokens, pos):
    tok_type, tok_val = tokens[pos]

    # unary negation
    if tok_type == "OP" and tok_val == "-":
        pos += 1
        node, value, pos = parse_factor(tokens, pos)
        return f"(neg {node})", -value, pos

    # unary plus not allowed
    if tok_type == "OP" and tok_val == "+":
        raise ValueError("Unary plus not allowed")

    # number token
    if tok_type == "NUM":
        pos += 1
        num = float(tok_val)
        return format_number(num), num, pos

    # parentheses expression
    if tok_type == "LPAREN":
        pos += 1
        node, value, pos = parse_expression(tokens, pos)

        if pos >= len(tokens) or tokens[pos][0] != "RPAREN":
            raise ValueError("Missing )")
        pos += 1
        return node, value, pos

    raise ValueError("Unexpected token")  # invalid token encountered


#HELPERS
# Format numbers for tree (integers without decimal)
def format_number(num):
    if float(num).is_integer():
        return str(int(num))
    return str(num)


# Format result for output
def format_result(val):
    # division by zero returns ERROR
    if val == float("inf") or val == float("-inf"):
        return "ERROR"

    if float(val).is_integer():
        return str(int(val))
    return f"{val:.4f}".rstrip("0").rstrip(".")


# ---- MAIN FUNCTION ----#
def evaluate_file(input_path: str) -> list[dict]:
    results = []
    out_lines = []

    # read input lines
    with open(input_path) as f:
        lines = [line.rstrip("\n") for line in f]

    # process each expression line
    for line in lines:
        record = {"input": line}

        try:
            # Step 1: Tokenize
            tokens = tokenize(line)
            token_str = format_tokens(tokens)

            # Step 2: Parse (build tree + compute value)
            node, value, pos = parse_expression(tokens, 0)

            # ensure no extra tokens left
            if tokens[pos][0] != "END":
                raise ValueError("Extra tokens")

            tree = node

            # Step 3: Format result
            result_value = value
            result_text = format_result(result_value)
            if result_text == "ERROR":
                result_value = "ERROR"

        except:
            # handle syntax errors, invalid chars, or division by zero
            tree = "ERROR"
            token_str = "ERROR"
            result_value = "ERROR"
            result_text = "ERROR"

        # save record
        record["tree"] = tree
        record["tokens"] = token_str
        record["result"] = result_value
        results.append(record)

        # prepare output for file
        out_lines.append(f"Input: {line}")
        out_lines.append(f"Tree: {tree}")
        out_lines.append(f"Tokens: {token_str}")
        out_lines.append(f"Result: {result_text}")
        out_lines.append("")

    # write output file in same folder as input
    out_path = os.path.join(os.path.dirname(input_path), "output.txt")
    with open(out_path, "w") as f:
        f.write("\n".join(out_lines).rstrip() + "\n")

    return results


# ---- ENTRY POINT ---- #
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "sample_input.txt")
    evaluate_file(input_file)