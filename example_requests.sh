echo "Check API Health"
curl -X 'GET' 'http://localhost:8000/health' -H 'accept: application/json'  -u 'alice:wonderland'

echo "\n\n"
echo "Verify credentials"
echo "Case 1: Credentials are valid"
curl -X 'GET' 'http://localhost:8000/admin/verify?username=clementine&password=mandarine' -H 'accept: application/json' -u 'alice:wonderland'
echo "\n"
echo "Case 2: Credentials are not valid"
curl -X 'GET' 'http://localhost:8000/admin/verify?username=machin&password=bidule' -H 'accept: application/json' -u 'alice:wonderland'

echo "\n\n"
echo "Request MCQ questions"
curl -X 'POST' 'http://localhost:8000/questions' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"use": "Test de positionnement", "subjects": ["BDD"], "num_questions": 3}' -u 'alice:wonderland' | jq
curl -X 'POST' 'http://localhost:8000/questions' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"use": "Test de validation", "subjects": ["classification"], "num_questions": 3}' -u 'alice:wonderland' | jq

echo "\n"
echo "Nombre de questions insuffisant"
curl -X 'POST' 'http://localhost:8000/questions' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"use": "Test de validation", "subjects": ["classification"], "num_questions": 39}' -u 'alice:wonderland' | jq

echo "\n\n"
echo "Add question if admin with password 4dm1N"
curl -X 'POST' 'http://localhost:8000/admin/add_question' -H 'accept: application/json'  -H 'Content-Type: application/json' -d '{"question": "Cassandra et HBase sont des bases de données","subject": "BDD","use": "Test de positionnement","responseA": "relationnelles", "responseB": "orientées objet", "responseC": "orientées colonne", "responseD": "orientées graphe", "correct": "C"}' -u 'admin:4dm1N' | jq
echo "\n"
echo "Add question if not admin"
curl -X 'POST' 'http://localhost:8000/admin/add_question' -H 'accept: application/json'  -H 'Content-Type: application/json' -d '{"question": "Cassandra et HBase sont des bases de données","subject": "BDD","use": "Test de positionnement","responseA": "relationnelles", "responseB": "orientées objet", "responseC": "orientées colonne", "responseD": "orientées graphe", "correct": "C"}' -u 'alice:wonderland' | jq

