"""Search and duplicate-check helpers for synthetic portfolio data."""
import re
from difflib import SequenceMatcher

ALIASES = {
    "battery": {"battery", "batteries", "baterai", "aki"},
    "tire": {"tire", "tires", "tyre", "tyres", "ban"},
    "filter": {"filter", "saringan"},
    "brake": {"brake", "rem"},
}

def normalize(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()

def expand_terms(query):
    tokens = normalize(query).split()
    expanded = set(tokens)
    for token in tokens:
        for group in ALIASES.values():
            if token in group or any(len(token) >= 3 and (token in word or word in token) for word in group):
                expanded.update(group)
    return expanded

def search_catalog(df, query, threshold=0.55):
    """Return matching rows with a simple transparent keyword score."""
    terms = expand_terms(query)
    fields = [c for c in ("pn", "description_en", "description_id", "category", "unit", "vendor", "brand") if c in df.columns]
    scores=[]
    for _, row in df.iterrows():
        text = normalize(" ".join(str(row.get(c, "")) for c in fields))
        words=set(text.split())
        score=0.0
        for term in terms:
            if term in words:
                score=max(score,1.0)
            elif words:
                score=max(score,max(SequenceMatcher(None,term,w).ratio() for w in words))
        scores.append(score)
    result=df.copy();result["match_score"]=scores
    return result[result.match_score>=threshold].sort_values("match_score",ascending=False)

def duplicate_fingerprint(pn, description, unit):
    """Strict duplicate key: normalized PN + description + unit."""
    return tuple(normalize(x) for x in (pn, description, unit))
