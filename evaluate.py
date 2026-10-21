"""Offline evaluation of a deterministic tool-authorization boundary, not an LLM."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent


def authorize(action, allowed_documents):
    if not isinstance(action,dict): return False
    if set(action)!={'tool','document_id'}: return False
    if action['tool']!='read_document': return False
    return isinstance(action['document_id'],str) and action['document_id'] in allowed_documents


def evaluate(cases):
    results=[]
    seen=set()
    for case in cases:
        if not isinstance(case,dict) or not isinstance(case.get('id'),str) or not case['id'].strip() or case['id'] in seen:
            raise ValueError('case IDs must be unique nonempty strings')
        allowed=case.get('allowed_documents')
        if not isinstance(allowed,list) or not all(isinstance(x,str) for x in allowed):
            raise ValueError('allowed_documents must be a list of strings')
        if type(case.get('expected_allowed')) is not bool: raise ValueError('expected_allowed must be boolean')
        actual=authorize(case.get('proposed_action'),set(allowed))
        results.append(dict(id=case['id'],allowed=actual,expected_allowed=case['expected_allowed'],passed=actual==case['expected_allowed']))
        seen.add(case['id'])
    return dict(evaluator='deterministic-authorization-v1',total=len(results),passed=sum(r['passed'] for r in results),results=results)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',nargs='?',type=Path,default=ROOT/'data/cases.json')
    args=parser.parse_args(argv)
    try:
        cases=json.loads(args.input.read_text(encoding='utf-8'))
        if not isinstance(cases,list): raise ValueError('expected a JSON list')
        result=evaluate(cases)
    except (ValueError,OSError) as exc:
        print(f'error: {exc}',file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result['passed']==result['total'] else 1


if __name__=='__main__': raise SystemExit(main())
