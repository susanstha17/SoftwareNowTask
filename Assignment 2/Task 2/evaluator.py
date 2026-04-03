import os

# ---------------- TOKENIZER ---------------- #

def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]

        if c.isspace():
            i += 1
            continue

        if c.isdigit() or c == '.':
            start = i
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            tokens.append(("NUM", expr[start:i]))
            continue

        if c in "+-*/":
            tokens.append(("OP", c))
            i += 1
            continue

        if c == "(":
            tokens.append(("LPAREN", "("))
            i += 1
            continue

        if c == ")":
            tokens.append(("RPAREN", ")"))
            i += 1
            continue

        raise ValueError("Invalid character")

    tokens.append(("END", ""))
    return tokens


def format_tokens(tokens):
    parts = []
    for t, v in tokens:
        if t == "END":
            parts.append("[END]")
        else:
            parts.append(f"[{t}:{v}]")
    return " ".join(parts)


# ---------------- PARSER ---------------- #

def parse_expression(tokens, pos):
    node, value, pos = parse_term(tokens, pos)

    while pos < len(tokens) and tokens[pos][0] == "OP" and tokens[pos][1] in "+-":
        op = tokens[pos][1]
        pos += 1
        right_node, right_val, pos = parse_term(tokens, pos)

        if op == "+":
            value = value + right_val
        else:
            value = value - right_val

        node = f"({op} {node} {right_node})"

    return node, value, pos


def parse_term(tokens, pos):
    node, value, pos = parse_factor(tokens, pos)

    while True:

        if tokens[pos][0] == "OP" and tokens[pos][1] in "*/":
            op = tokens[pos][1]
            pos += 1

        elif tokens[pos][0] in ("NUM", "LPAREN") or (
            tokens[pos][0] == "OP" and tokens[pos][1] == "-"
        ):
            op = "*"
        else:
            break

        right_node, right_val, pos = parse_factor(tokens, pos)

        if op == "*":
            value = value * right_val
        else:
            value = value / right_val

        node = f"({op} {node} {right_node})"

    return node, value, pos


def parse_factor(tokens, pos):
    tok_type, tok_val = tokens[pos]

    if tok_type == "OP" and tok_val == "-":
        pos += 1
        node, value, pos = parse_factor(tokens, pos)
        return f"(neg {node})", -value, pos

    if tok_type == "OP" and tok_val == "+":
        raise ValueError("Unary plus not allowed")

    if tok_type == "NUM":
        pos += 1
        num = float(tok_val)
        text = format_number(num)
        return text, num, pos

    if tok_type == "LPAREN":
        pos += 1
        node, value, pos = parse_expression(tokens, pos)

        if tokens[pos][0] != "RPAREN":
            raise ValueError("Missing )")

        pos += 1
        return node, value, pos

    raise ValueError("Unexpected token")


# ---------------- HELPERS ---------------- #

def format_number(num):
    if float(num).is_integer():
        return str(int(num))
    return str(num)


def format_result(val):
    if float(val).is_integer():
        return str(int(val))
    return f"{val:.4f}".rstrip("0").rstrip(".")


# ---------------- MAIN FUNCTION ---------------- #

def evaluate_file(input_path: str) -> list[dict]:

    results = []
    out_lines = []

    with open(input_path) as f:
        lines = [line.rstrip("\n") for line in f]

    for line in lines:

        record = {"input": line}

        try:
            tokens = tokenize(line)
            token_str = format_tokens(tokens)

            node, value, pos = parse_expression(tokens, 0)

            if tokens[pos][0] != "END":
                raise ValueError("Extra tokens")

            result_value = value
            tree = node

            try:
                result_text = format_result(result_value)
            except:
                result_text = "ERROR"
                result_value = "ERROR"

        except:
            tree = "ERROR"
            token_str = "ERROR"
            result_text = "ERROR"
            result_value = "ERROR"

        record["tree"] = tree
        record["tokens"] = token_str
        record["result"] = result_value

        results.append(record)

        out_lines.append(f"Input: {line}")
        out_lines.append(f"Tree: {tree}")
        out_lines.append(f"Tokens: {token_str}")
        out_lines.append(f"Result: {result_text}")
        out_lines.append("")

    out_path = os.path.join(os.path.dirname(input_path), "sample_output.txt")

    with open(out_path, "w") as f:
        f.write("\n".join(out_lines).rstrip() + "\n")

    return results



if __name__ == "__main__":
    evaluate_file("Assignment 2/Task 2/sample_input.txt")