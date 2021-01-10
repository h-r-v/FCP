		// Program starts here. Creates a sample graph in the
		// DOM node with the specified ID. This function is invoked
		// from the onLoad event handler of the document (see below).

function main()
		{
			// Checks if browser is supported
			if (!mxClient.isBrowserSupported())
			{
				// Displays an error message if the browser is
				// not supported.
				mxUtils.error('Browser is not supported!', 200, false);
			}
			else
			{
				// Defines an icon for creating new connections in the connection handler.
				// This will automatically disable the highlighting of the source vertex.
				mxConnectionHandler.prototype.connectImage = new mxImage('images/connector.gif', 16, 16);

				var primaryColor = 'red';//'#cf0000';
				var secondaryColor = 'black'; //"#f0eded";

				// Creates the div for the toolbar
				var tbContainer = document.createElement('div');
				tbContainer.style.position = 'absolute';
				tbContainer.style.overflow = 'hidden';
				tbContainer.style.padding = '2px';
				tbContainer.style.left = '0px';
				tbContainer.style.top = '0px';
				tbContainer.style.width = '2%';
				tbContainer.style.bottom = '0px';
				tbContainer.style.minWidth = '40px';
				tbContainer.id = 'toolBar';

				tbContainer.style.backgroundColor = primaryColor;
				
				document.body.appendChild(tbContainer);
			
				// Creates new toolbar without event processing
				var toolbar = new mxToolbar(tbContainer);
				toolbar.enabled = false
				
				// Creates the div for the graph
				var container = document.createElement('div');
				container.style.position = 'absolute';
				container.style.overflow = 'scroll';
				container.style.left = '43px';
				container.style.top = '4%';
				container.style.right = '0px';
				container.style.bottom = '0px';
				container.style.width = '67.6%';
				container.style.background = 'url("/images/grid.gif")';
				container.id = 'mainGraph';

				document.body.appendChild(container);

				// Div for util buttons, ex: undo, redo, zoom in, zoom out
				var uButtons = document.createElement('div');
				uButtons.style.position = 'absolute';
				uButtons.style.overflow = 'hidden';
				uButtons.style.left = '40px';
				uButtons.style.top = '0px';
				uButtons.style.right = '0px';
				uButtons.style.width = '68%';
				uButtons.style.height = '4%';
				uButtons.style.minHeight = '40px';
				uButtons.id = 'uButtons';

				uButtons.style.backgroundColor = primaryColor;

				document.body.appendChild(uButtons);

				// Div for generated code
				var codeBox = document.createElement('div');
				codeBox.style.position = 'absolute';
				codeBox.style.overflow = 'scroll';
				codeBox.style.float = 'right'
				codeBox.style.top = '0px';
				codeBox.style.right = '0px';
				codeBox.style.bottom = '0px';
				codeBox.style.width = "30%";
				codeBox.style.height = "35%";
				codeBox.id = 'codeBox';

				codeBox.style.backgroundColor = secondaryColor;

				document.body.appendChild(codeBox);

				// Div for executedOP
				var execBox = document.createElement('div');
				execBox.style.position = 'absolute';
				execBox.style.overflow = 'scroll';
				execBox.style.float = 'right'
				execBox.style.top = '35%';
				execBox.style.right = '0px';
				execBox.style.bottom = '0px';
				execBox.style.width = "30%";
				execBox.style.height = "35%";
				execBox.id = 'execBox';

				execBox.style.backgroundColor = 'grey';

				document.body.appendChild(execBox);

				// Default text inside codeBox
				var prev = document.createElement('pre');
				prev.style.id = 'code';
				prev.style.color = 'green';
				prev.style.fontSize = '20px';
				prev.style.paddingLeft = '15px';
				prev.innerHTML = "Press preview after putting in the link to see the options available to you.";
				codeBox.appendChild(prev);

				// Default text inside codeBox
				var preve = document.createElement('pre');
				preve.style.id = 'code';
				preve.style.color = 'black';
				preve.style.fontSize = '20px';
				preve.style.paddingLeft = '15px';
				preve.innerHTML = "Output(s):";
				execBox.appendChild(preve);

				// Div for execute and download buttons
				var buttonBox = document.createElement('div');
				buttonBox.style.position = 'absolute';
				buttonBox.style.overflow = 'hidden';
				buttonBox.style.float = 'right'
				buttonBox.style.top = '70%';
				buttonBox.style.right = '0px';
				buttonBox.style.bottom = '0px';
				buttonBox.style.width = "30%";
				buttonBox.style.height = "30%"
				buttonBox.id = 'buttonBox';

				buttonBox.style.backgroundColor = primaryColor;

				document.body.appendChild(buttonBox);
				
				// Workaround for Internet Explorer ignoring certain styles
				if (mxClient.IS_QUIRKS)
				{
					document.body.style.overflow = 'hidden';
					new mxDivResizer(tbContainer);
					new mxDivResizer(container);
				}
	
				// Creates the model and the graph inside the container
				// using the fastest rendering available on the browser
				var model = new mxGraphModel();
				var graph = new mxGraph(container, model);

				// Enables new connections in the graph
				graph.setConnectable(true);
				graph.setMultigraph(false);

				// Stops editing on enter or escape keypress
				var keyHandler = new mxKeyHandler(graph);
				var rubberband = new mxRubberband(graph);
				
				var addVertex = function(icon, w, h, style)
				{
					var vertex = new mxCell(null, new mxGeometry(0, 0, w, h), style);
					vertex.setVertex(true);
				
					var img = addToolbarItem(graph, toolbar, vertex, icon);
					img.enabled = true;
					
					graph.getSelectionModel().addListener(mxEvent.CHANGE, function()
					{
						var tmp = graph.isSelectionEmpty();
						img.enabled = tmp;
					});
                };

				//addVertex('static/shapes/ellipse.png', 100, 100, 'shape=ellipse');				
				addVertex('static/shapes/rectangle.png', 100, 100, 'shape=rectangle');
                //addVertex('static/shapes/rhombus.png', 100, 100, 'shape=rhombus');
				addVertex('static/shapes/swimlane.gif', 100, 100, 'shape=swimlane');
				//addVertex('static/shapes/hexagon.png', 100, 100, 'shape=hexagon');
				//addVertex('static/shapes/cloud.png', 100, 100, 'shape=cloud');

				//Help button
				helpButton = document.createElement('button');
				helpButton.style.bottom = '0px';
				helpButton.style.left = '-10px';
				helpButton.style.padding = '0px'
				helpButton.style.position = 'absolute';
				helpButton.innerHTML = "<img src='images/help32x32.png' width=32 height=32>";
				helpButton.onclick = helpPage
				helpButton.id = 'helpButton';

				document.getElementById('toolBar').appendChild(helpButton);
				
				//Shows icons if the mouse is over a cell
				var iconTolerance = 20;
				graph.addMouseListener(
				{
				     currentState: null,
				     currentIconSet: null,
				     mouseDown: function(sender, me)
				     {
				       // Hides icons on mouse down
				         if (this.currentState != null)
				         {
				             this.dragLeave(me.getEvent(), this.currentState);
				             this.currentState = null;
				         }
				     },
				     mouseMove: function(sender, me)
				     {
				       if (this.currentState != null && (me.getState() == this.currentState || me.getState() == null))
				       {
				         var tol = iconTolerance;
				         var tmp = new mxRectangle(me.getGraphX() - tol,
				           me.getGraphY() - tol, 2 * tol, 2 * tol);

				         if (mxUtils.intersects(tmp, this.currentState))
				         {
				           return;
				         }
				       }
				     var tmp = graph.view.getState(me.getCell());
				       // Ignores everything but vertices
				     if (graph.isMouseDown || (tmp != null && !graph.getModel().isVertex(tmp.cell)))
				     {
				       tmp = null;
				     }
				         if (tmp != this.currentState)
				         {
				           if (this.currentState != null)
				           {
				               this.dragLeave(me.getEvent(), this.currentState);
				           }
				           this.currentState = tmp;
				           if (this.currentState != null)
				           {
				               this.dragEnter(me.getEvent(), this.currentState);
				           }
				         }
				     },
				     mouseUp: function(sender, me) { },
				     dragEnter: function(evt, state)
				     {
				       if (this.currentIconSet == null)
				       {
				         this.currentIconSet = new mxIconSet(state);
				       }
				     },
				     dragLeave: function(evt, state)
				     {
				       if (this.currentIconSet != null)
				       {
				         this.currentIconSet.destroy();
				         this.currentIconSet = null;
				       }
				     }
				 });
				 //Icon mouse over ends here.

				//undo/redo manager
				var undoManager = new mxUndoManager();
				var listener = function(sender, evt)
					{
						undoManager.undoableEditHappened(evt.getProperty('edit'));
					};
			
				graph.getModel().addListener(mxEvent.UNDO, listener);
				graph.getView().addListener(mxEvent.UNDO, listener);
				
				// upper butons
				// UNDO
				var undoButton = document.createElement('button');
				undoButton.innerHTML = "<img src='images/undo.png' width=32 height=32>";
				undoButton.style.position = 'relative';
				undoButton.style.padding = '4px 25px 0px 5px';
				undoButton.style.float = 'right';
				undoButton.style.backgroundColor = 'Transparent';
				undoButton.style.borderStyle = 'none';
				undoButton.onclick = function(){undoManager.undo();}

				document.getElementById('uButtons').appendChild(undoButton);
				
				// REDO
				var redoButton = document.createElement('button');
				redoButton.innerHTML = "<img src='images/redo.png' width=32 height=32>";
				redoButton.style.position = 'relative';
				redoButton.style.padding = '4px 5px 0px 5px';
				redoButton.style.float = 'right';
				redoButton.style.backgroundColor = 'Transparent';
				redoButton.style.borderStyle = 'none';
				redoButton.onclick = function(){undoManager.redo();}
				document.getElementById('uButtons').appendChild(redoButton);
				
				// ZOOMIN
				var zinButton = document.createElement('button');
				zinButton.innerHTML = "<img src='images/zoom_in.png' width=32 height=32>";
				zinButton.style.position = 'relative';
				zinButton.style.padding = '4px 5px 0px 5px';
				zinButton.style.float = 'right';
				zinButton.style.backgroundColor = 'Transparent';
				zinButton.style.borderStyle = 'none';
				zinButton.onclick = function(){graph.zoomIn();}
				document.getElementById('uButtons').appendChild(zinButton);
				
				// ZOOMOUT
				var zoutButton = document.createElement('button');
				zoutButton.innerHTML = "<img src='images/zoom_out.png' width=32 height=32>";
				zoutButton.style.position = 'relative';
				zoutButton.style.padding = '4px 5px 0px 5px';
				zoutButton.style.float = 'right';
				zoutButton.style.backgroundColor = 'Transparent';
				zoutButton.style.borderStyle = 'none';
				zoutButton.onclick = function(){graph.zoomOut();}
				document.getElementById('uButtons').appendChild(zoutButton);

				// buttonBox
				//preview
				var previewButton = document.createElement('button');
				previewButton.id = 'previewButton';
				previewButton.innerHTML = "Preview Options";
				previewButton.onclick = function()
				{
					var encoder = new mxCodec();
					var node = encoder.encode(graph.getModel());
					var testString = mxUtils.getXml(node);
					var result = xmlToJSON.parseString(testString);
					var json = JSON.stringify(result);

					$.ajax({
						type: 'POST',
						 url: "/getsmartpreview",
						 data: {"myKey": json},
						 success: function (data) {

							var prev = document.createElement('pre');
							prev.innerHTML=data;
							prev.style.color = 'green';
							prev.style.id = 'code';
							prev.style.fontSize = '20px';
							prev.style.paddingLeft = '15px';
							document.getElementById('codeBox').replaceChild(prev, document.getElementById('codeBox').childNodes[0]);
						 }
					   });
				}
				document.getElementById('buttonBox').appendChild(previewButton);

				//execute
				var execButton = document.createElement('button');
				execButton.id = 'execButton';
				execButton.innerHTML = "Execute FlowChart";
				execButton.onclick = function()
				{
					var encoder = new mxCodec();
					var node = encoder.encode(graph.getModel());
					var testString = mxUtils.getXml(node);
					var result = xmlToJSON.parseString(testString);
					var json = JSON.stringify(result);

					$.ajax({
						type: 'POST',
						 url: "/smartexec",
						 data: {"myKey": json},
						 success: function (data) {
							var preve = document.createElement('pre');
							preve.innerHTML=data;
							preve.style.color = 'Black';
							preve.style.id = 'code';
							preve.style.fontSize = '20px';
							preve.style.paddingLeft = '15px';
							document.getElementById('execBox').appendChild(preve);
						 }
					   });
				}
				document.getElementById('buttonBox').appendChild(execButton);

				// style for lower left buttons
				var nodes = document.getElementById('buttonBox').childNodes;
				for(var i=0; i<nodes.length; i++) 
				{
						nodes[i].style.background = primaryColor;
						nodes[i].style.height = '50%';
						nodes[i].style.width = '100%';	
						nodes[i].style.fontSize = '20px';
				}
			}
		}

function addToolbarItem(graph, toolbar, prototype, image)
		{
			// Function that is executed when the image is dropped on
			// the graph. The cell argument points to the cell under
			// the mousepointer if there is one.
			var funct = function(graph, evt, cell, x, y)
			{
				graph.stopEditing(false);

				var vertex = graph.getModel().cloneCell(prototype);
				vertex.geometry.x = x;
				vertex.geometry.y = y;
					
				graph.addCell(vertex);
				graph.setSelectionCell(vertex);
			}
			
			// Creates the image which is used as the drag icon (preview)
			var img = toolbar.addMode(null, image, function(evt, cell)
			{
				var pt = this.graph.getPointForEvent(evt);
				funct(graph, evt, cell, pt.x, pt.y);
			});
			
			// Disables dragging if element is disabled. This is a workaround
			// for wrong event order in IE. Following is a dummy listener that
			// is invoked as the last listener in IE.
			mxEvent.addListener(img, 'mousedown', function(evt)
			{
				// do nothing
			});
			
			// This listener is always called first before any other listener
			// in all browsers.
			mxEvent.addListener(img, 'mousedown', function(evt)
			{
				if (img.enabled == false)
				{
					mxEvent.consume(evt);
				}
			});
						
			mxUtils.makeDraggable(img, graph, funct);
			
			return img;
		}

// The Icon Function
function mxIconSet(state)
	{
	this.images = [];
	var graph = state.view.graph;

	// Copy Icon that can found on the right bottom of the vertx
	var img = mxUtils.createImage("images/copy.png");
	img.setAttribute('title', 'Duplicate');
	img.style.position = 'absolute';
	img.style.cursor = 'pointer';
	img.style.width = '16px';
	img.style.height = '16px';
	img.style.left = (state.x + state.width) + 'px';
	img.style.top = (state.y + state.height) + 'px';

	mxEvent.addGestureListeners(img,
		mxUtils.bind(this, function(evt)
		{
		var s = graph.gridSize;
		graph.setSelectionCells(graph.moveCells([state.cell], s, s, true));
		mxEvent.consume(evt);
		this.destroy();
		})
	);

	state.view.graph.container.appendChild(img);
	this.images.push(img);

	// Delete Icon that can found on the right top of the vertex
	var img = mxUtils.createImage('images/delete2.png');
	img.setAttribute('title', 'Delete');
	img.style.position = 'absolute';
	img.style.cursor = 'pointer';
	img.style.width = '16px';
	img.style.height = '16px';
	img.style.left = (state.x + state.width) + 'px';
	img.style.top = (state.y - 16) + 'px';

	mxEvent.addGestureListeners(img,
		mxUtils.bind(this, function(evt)
		{
		// Disables dragging the image
		mxEvent.consume(evt);
		})
	);

	mxEvent.addListener(img, 'click',
		mxUtils.bind(this, function(evt)
		{
		graph.removeCells([state.cell]);
		mxEvent.consume(evt);
		this.destroy();
		})
	);

	state.view.graph.container.appendChild(img);
	this.images.push(img);
	};



mxIconSet.prototype.destroy = function()
	{
	if (this.images != null)
	{
		for (var i = 0; i < this.images.length; i++)
		{
		var img = this.images[i];
		img.parentNode.removeChild(img);
		}
	}

	this.images = null;
	};

var xmlToJSON = (function () {

	this.version = "1.3.4";
 
	var options = { // set up the default options
		mergeCDATA: true, // extract cdata and merge with text
		grokAttr: true, // convert truthy attributes to boolean, etc
		grokText: true, // convert truthy text/attr to boolean, etc
		normalize: true, // collapse multiple spaces to single space
		xmlns: true, // include namespaces as attribute in output
		namespaceKey: '_ns', // tag name for namespace objects
		textKey: '_text', // tag name for text nodes
		valueKey: '_value', // tag name for attribute values
		attrKey: '_attr', // tag for attr groups
		cdataKey: '_cdata', // tag for cdata nodes (ignored if mergeCDATA is true)
		attrsAsObject: true, // if false, key is used as prefix to name, set prefix to '' to merge children and attrs.
		stripAttrPrefix: true, // remove namespace prefixes from attributes
		stripElemPrefix: true, // for elements of same name in diff namespaces, you can enable namespaces and access the nskey property
		childrenAsArray: true // force children into arrays
	};
 
	var prefixMatch = new RegExp(/(?!xmlns)^.*:/);
	var trimMatch = new RegExp(/^\s+|\s+$/g);
 
	this.grokType = function (sValue) {
		if (/^\s*$/.test(sValue)) {
			return null;
		}
		if (/^(?:true|false)$/i.test(sValue)) {
			return sValue.toLowerCase() === "true";
		}
		if (isFinite(sValue)) {
			return parseFloat(sValue);
		}
		return sValue;
	};
 
	this.parseString = function (xmlString, opt) {
		return this.parseXML(this.stringToXML(xmlString), opt);
	}
 
	this.parseXML = function (oXMLParent, opt) {
 
		// initialize options
		for (var key in opt) {
			options[key] = opt[key];
		}
 
		var vResult = {},
			nLength = 0,
			sCollectedTxt = "";
 
		// parse namespace information
		if (options.xmlns && oXMLParent.namespaceURI) {
			vResult[options.namespaceKey] = oXMLParent.namespaceURI;
		}
 
		// parse attributes
		// using attributes property instead of hasAttributes method to support older browsers
		if (oXMLParent.attributes && oXMLParent.attributes.length > 0) {
			var vAttribs = {};
 
			for (nLength; nLength < oXMLParent.attributes.length; nLength++) {
				var oAttrib = oXMLParent.attributes.item(nLength);
				vContent = {};
				var attribName = '';
 
				if (options.stripAttrPrefix) {
					attribName = oAttrib.name.replace(prefixMatch, '');
 
				} else {
					attribName = oAttrib.name;
				}
 
				if (options.grokAttr) {
					vContent[options.valueKey] = this.grokType(oAttrib.value.replace(trimMatch, ''));
				} else {
					vContent[options.valueKey] = oAttrib.value.replace(trimMatch, '');
				}
 
				if (options.xmlns && oAttrib.namespaceURI) {
					vContent[options.namespaceKey] = oAttrib.namespaceURI;
				}
 
				if (options.attrsAsObject) { // attributes with same local name must enable prefixes
					vAttribs[attribName] = vContent;
				} else {
					vResult[options.attrKey + attribName] = vContent;
				}
			}
 
			if (options.attrsAsObject) {
				vResult[options.attrKey] = vAttribs;
			} else { }
		}
 
		// iterate over the children
		if (oXMLParent.hasChildNodes()) {
			for (var oNode, sProp, vContent, nItem = 0; nItem < oXMLParent.childNodes.length; nItem++) {
				oNode = oXMLParent.childNodes.item(nItem);
 
				if (oNode.nodeType === 4) {
					if (options.mergeCDATA) {
						sCollectedTxt += oNode.nodeValue;
					} else {
						if (vResult.hasOwnProperty(options.cdataKey)) {
							if (vResult[options.cdataKey].constructor !== Array) {
								vResult[options.cdataKey] = [vResult[options.cdataKey]];
							}
							vResult[options.cdataKey].push(oNode.nodeValue);
 
						} else {
							if (options.childrenAsArray) {
								vResult[options.cdataKey] = [];
								vResult[options.cdataKey].push(oNode.nodeValue);
							} else {
								vResult[options.cdataKey] = oNode.nodeValue;
							}
						}
					}
				} /* nodeType is "CDATASection" (4) */
				else if (oNode.nodeType === 3) {
					sCollectedTxt += oNode.nodeValue;
				} /* nodeType is "Text" (3) */
				else if (oNode.nodeType === 1) { /* nodeType is "Element" (1) */
 
					if (nLength === 0) {
						vResult = {};
					}
 
					// using nodeName to support browser (IE) implementation with no 'localName' property
					if (options.stripElemPrefix) {
						sProp = oNode.nodeName.replace(prefixMatch, '');
					} else {
						sProp = oNode.nodeName;
					}
 
					vContent = xmlToJSON.parseXML(oNode);
 
					if (vResult.hasOwnProperty(sProp)) {
						if (vResult[sProp].constructor !== Array) {
							vResult[sProp] = [vResult[sProp]];
						}
						vResult[sProp].push(vContent);
 
					} else {
						if (options.childrenAsArray) {
							vResult[sProp] = [];
							vResult[sProp].push(vContent);
						} else {
							vResult[sProp] = vContent;
						}
						nLength++;
					}
				}
			}
		} else if (!sCollectedTxt) { // no children and no text, return null
			if (options.childrenAsArray) {
				vResult[options.textKey] = [];
				vResult[options.textKey].push(null);
			} else {
				vResult[options.textKey] = null;
			}
		}
 
		if (sCollectedTxt) {
			if (options.grokText) {
				var value = this.grokType(sCollectedTxt.replace(trimMatch, ''));
				if (value !== null && value !== undefined) {
					vResult[options.textKey] = value;
				}
			} else if (options.normalize) {
				vResult[options.textKey] = sCollectedTxt.replace(trimMatch, '').replace(/\s+/g, " ");
			} else {
				vResult[options.textKey] = sCollectedTxt.replace(trimMatch, '');
			}
		}
 
		return vResult;
	}
 
 
	// Convert xmlDocument to a string
	// Returns null on failure
	this.xmlToString = function (xmlDoc) {
		try {
			var xmlString = xmlDoc.xml ? xmlDoc.xml : (new XMLSerializer()).serializeToString(xmlDoc);
			return xmlString;
		} catch (err) {
			return null;
		}
	}
 
	// Convert a string to XML Node Structure
	// Returns null on failure
	this.stringToXML = function (xmlString) {
		try {
			var xmlDoc = null;
 
			if (window.DOMParser) {
 
				var parser = new DOMParser();
				xmlDoc = parser.parseFromString(xmlString, "text/xml");
 
				return xmlDoc;
			} else {
				xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
				xmlDoc.async = false;
				xmlDoc.loadXML(xmlString);
 
				return xmlDoc;
			}
		} catch (e) {
			return null;
		}
	}
 
	return this;
 }).call({});

function helpPage()
{
	window.open( "smart rules.html", "_blank"); 
}
